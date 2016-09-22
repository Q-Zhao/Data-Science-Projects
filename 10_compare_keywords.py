# -*- coding: utf-8 -*-

import json
from TwitterPlot import generic_bar_plot


def load_data(filename):
	f = open(filename,'r', encoding='utf-8').read()
	content_json = json.loads(f)
	return content_json

def compare_words(data, lst):
	words_dict = {}
	for word in lst:
		if isinstance(word, str):
			words_dict[word] = 0
		elif isinstance(word, list) and len(word)!=0:
			words_dict[word[0]]	= 0
	for tweet in data:
		if "text" in tweet.keys():
			sentence = tweet["text"]
			for word in lst:
				if isinstance(word, str) and word.lower() in sentence:
					words_dict[word] += 1
				elif isinstance(word, list):
					for candidate in word:
						if candidate.lower() in sentence:
							words_dict[word[0]] += 1
	return words_dict


queries = ['camera', ['headphone', 'earphone'], ["Lighting", "3.5"]]
tweets_09_10 = load_data("combined_all.json")
compare_words_info = compare_words(tweets_09_10, queries)
generic_bar_plot(compare_words_info)


