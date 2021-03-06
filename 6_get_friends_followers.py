import twitter
import io
import os
from functools import partial
from sys import maxsize
import sys
import time
from urllib.error import URLError 
from http.client import BadStatusLine
import json
import twitter


def oauth_login():
	CONSUMER_KEY = ''
	CONSUMER_SECRET =''
	OAUTH_TOKEN = ''
	OAUTH_TOKEN_SECRET = ''

	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
	                           CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api

def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw):
	def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):
		if wait_period > 3600: # Seconds
			print >> sys.stderr, 'Too many retries. Quitting.'
			raise e
		if e.e.code == 401:
			print >> sys.stderr, 'Encountered 401 Error (Not Authorized)'
			return None
		elif e.e.code == 404:
			print >> sys.stderr, 'Encountered 404 Error (Not Found)'
			return None
		elif e.e.code == 429:
			print >> sys.stderr, 'Encountered 429 Error (Rate Limit Exceeded)'
			if sleep_when_rate_limited:
				print >> sys.stderr, "Retrying in 15 minutes...ZzZ..."
				sys.stderr.flush()
				time.sleep(60*15 + 5)
				print >> sys.stderr, '...ZzZ...Awake now and trying again.'
				return 2
			else:
				raise e # Caller must handle the rate limiting issue
		elif e.e.code in (500, 502, 503, 504):
			print >> sys.stderr, 'Encountered %i Error. Retrying in %i seconds' % \
					(e.e.code, wait_period)
			time.sleep(wait_period)
			wait_period *= 1.5
			return wait_period
		else:
			raise e
	wait_period = 2
	error_count = 0
	while True:
		try:
			return twitter_api_func(*args, **kw)
		except twitter.api.TwitterHTTPError as e:
			error_count = 0
			wait_period = handle_twitter_http_error(e, wait_period)
			if wait_period is None:
				return
		except URLError as e:
			error_count += 1
			print >> sys.stderr, "URLError encountered. Continuing."
			if error_count > max_errors:
				print >> sys.stderr, "Too many consecutive errors...bailing out."
				raise
		except BadStatusLine as e:
			error_count += 1
			print >> sys.stderr, "BadStatusLine encountered. Continuing."
			if error_count > max_errors:
				print >> sys.stderr, "Too many consecutive errors...bailing out."
				raise


def get_friends_followers_ids(twitter_api, screen_name=None, user_id=None, friends_limit=maxsize, followers_limit=maxsize):

	assert (screen_name != None) != (user_id != None), \
	"Must have screen_name or user_id, but not both"

	get_friends_ids = partial(make_twitter_request, twitter_api.friends.ids, count=5000)
	get_followers_ids = partial(make_twitter_request, twitter_api.followers.ids, count=5000)

	friends_ids, followers_ids = [], []

	for twitter_api_func, limit, ids, label in [
				[get_friends_ids, friends_limit, friends_ids, "friends"], 
					[get_followers_ids, followers_limit, followers_ids, "followers"]
				]:
		
		if limit == 0: continue
			
		cursor = -1
		while cursor != 0:
			if screen_name: 
				response = twitter_api_func(screen_name=screen_name, cursor=cursor)
			else: 
				response = twitter_api_func(user_id=user_id, cursor=cursor)

			if response is not None:
				ids += response['ids']
				cursor = response['next_cursor']
			print('Fetched {0} total {1} ids for {2}'.format(len(ids),label, (user_id or screen_name)))

			if len(ids) >= limit or response is None:
				break
	return friends_ids[:friends_limit], followers_ids[:followers_limit]


def save_json(fname, data):
	a = []
	if not os.path.isfile(fname):
	    a.append(data)
	    with open(fname, mode='w') as f:
	        f.write(json.dumps(a, indent=2))
	else:
	    with open(fname) as feedsjson:
	        feeds = json.load(feedsjson)
	    feeds.append(data)
	    with open(fname, mode='w') as f:
	        f.write(json.dumps(feeds, indent=2))


twitter_api = oauth_login()
friends_ids, followers_ids = get_friends_followers_ids(twitter_api, 
                                                       screen_name="tim_cook", 
                                                       friends_limit=200, 
                                                       followers_limit=200)

for friend_id in friends_ids:
	friend_info = twitter_api.users.lookup(user_id = friend_id)
	save_json("cook_friends_info.json", friend_info)


for follower_id in followers_ids:
	follower_info = twitter_api.users.lookup(user_id = follower_id)
	save_json("cook_followers_info.json", follower_info)
	






