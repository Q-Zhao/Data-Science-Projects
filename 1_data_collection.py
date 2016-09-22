import twitter
import os
import sys
import json

# Standard Twitter API acess
def oauth_login():
	CONSUMER_KEY = ''
	CONSUMER_SECRET =''
	OAUTH_TOKEN = ''
	OAUTH_TOKEN_SECRET = ''
	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
	                           CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api

# save_json_in_one_file function allows team members to save all data into one json file even with different access informations
def save_json_in_one_file(fname, data):
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

# save_json_seperately function allows team members to save their own json file seperately
def save_json_seperately(filename, data):
	with io.open(filename,'a+', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=3))
        f.write(',\n')

# Need to combine seperate json files from team members by calling one of combining functions.
# first function is combining two file1 and file2 to a newfile
def combine_two_files(file1, file2, newfile):
	f1 = open(file1, 'r', encoding='utf-8')
	f2 = open(file2, 'r', encoding='utf-8')
	content_1 = json.loads(f1.read())
	content_2 = json.loads(f2.read())
	content = content_2+content_1
	f = open(newfile, 'w', encoding='utf-8')
	f.write(json.dumps(content, indent=2))
	f1.close()
	f2.close()
	f.close()

# second function is combining a list of file names to a newfile in order.
def combine_multiple_files(file_lst_inorder, newfile): 
	content = list()
	for i in range(len(file_lst_inorder)):
		file_open = open(file_lst_inorder[i], 'r', encoding='utf-8')
		content +=  json.loads(file_open.read())	
		file_open.close()
	with open(newfile, 'w', encoding='utf-8') as new_file:
		new_file.write(json.dumps(content, indent=2))


twitter_api = oauth_login()
q = 'iphone 7, Iphone7, iphone7, Iphone 7' 
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
stream = twitter_stream.statuses.filter(track=q)

for tweet in stream:
	save_json_in_one_file('OneDataBase.json', tweet)

