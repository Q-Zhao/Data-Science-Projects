import twitter, sys, io, json, os

def load_data(filename):
	f = open(filename,'r', encoding='utf-8').read()
	content_json = json.loads(f)
	return content_json

def extract_tweet_entities(statuses):
	screen_names, hashtags, urls, medias, symbols = [], [], [], [], []
	if len(statuses) == 0:
		return [], [], [], [], []
	for status in statuses:
		if "entities" in status.keys():
			if len(status['entities']['user_mentions']) != 0:
				for user_mention in status['entities']['user_mentions']:
					screen_names.append(user_mention['screen_name'])

			if len(status['entities']['hashtags']) != 0:
				for hashtag in status['entities']['hashtags']:
					hashtags.append(hashtag['text'])

			if len(status['entities']['urls']) != 0:
				for url in status['entities']['urls']:
					urls.append(url['expanded_url'])

			if len(status['entities']['symbols']) != 0:
				for symbol in status['entities']['symbols']:
					symbols.append(symbol['text'])

			if "media" in status['entities'].keys() and len(status['entities']['media']) != 0:
					for media in status['entities']['media']:
						medias.append(media['url'])

	return screen_names, hashtags, urls, medias, symbols

content = load_data('combined_all.json')
screen_names, hashtags, urls, media, symbols = extract_tweet_entities(content)


print("screen_name: ", json.dumps(screen_names[0:5], indent=1))
print("hashtags: ", json.dumps(hashtags[0:5], indent=1))
print("urls: ", json.dumps(urls[0:5], indent=1))
print("media: ", json.dumps(media[0:5], indent=1))
print("Screen_name: ", json.dumps(symbols[0:5], indent=1))