# -*- coding: utf-8 -*-
import nltk
import json
from nltk.corpus import twitter_samples, stopwords
import string

negative_tweets_abs = twitter_samples.abspath("negative_tweets.json")
positive_tweets_abs = twitter_samples.abspath("positive_tweets.json")
negative_word_tokenized = twitter_samples.tokenized(negative_tweets_abs)
positive_word_tokenized = twitter_samples.tokenized(positive_tweets_abs)

def unwanted():
	unwanted = list(stopwords.words('english'))
	unwanted += list(string.punctuation)
	return unwanted 

unwanted_words_list = unwanted()

def clean_up_word_set(ls):
	word_set = []
	for l in ls:
		for word in l:
			if word not in unwanted_words_list and word not in word_set:
				word_set.append(word)
	return word_set

negative_words = clean_up_word_set(negative_word_tokenized)
positive_words = clean_up_word_set(positive_word_tokenized)

with open("negative_words_cleaned.json", "w", encoding='utf-8') as f_neg:
	f_neg.write(json.dumps(negative_words, indent=3))

with open("positive_words_cleaned.json", "w", encoding='utf-8') as f_pos:
	f_pos.write(json.dumps(positive_words, indent=3))

