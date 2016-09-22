# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize
import json
from nltk.corpus import twitter_samples, stopwords
import string
import matplotlib.pyplot as plt
from TwitterPlot import generic_pie_plot

def load_data(filename):
	with open(filename,'r', encoding='utf-8') as f:
		text = f.read()
	content_json = json.loads(text)
	return content_json

def estimate_features(data, negative_words, positive_words):
	data_strings = []
	for tweet in data:
		if "lang" in tweet.keys() and tweet["lang"]=="en" and "text" in tweet.keys() and len(tweet["text"])!=0:
			data_strings.append(tweet["text"])
	scores_map = {}
	for sentence in data_strings:
		score = 0
		words_list = word_tokenize(sentence)
		for word in words_list:
			if word in negative_words:
				score -= 1
			if word in positive_words:
				score += 1
		scores_map[score] = scores_map.get(score, 0) + 1
	sorted_scores = sorted(scores_map.items(), key=lambda t: t[0], reverse=True)
	return sorted_scores

def positive_negative_map(score_map):
	p_n_map = {"positive":0, "negative":0, "neutral":0}
	for pair in score_map:
		if pair[0]>0:
			p_n_map["positive"] += pair[1]
		elif pair[0] == 0:
			p_n_map["neutral"] += pair[1]
		else:
			p_n_map["negative"] += pair[1]
	return p_n_map


negative_words = load_data("negative_words_cleaned.json")
positive_words = load_data("positive_words_cleaned.json")
data_strings = load_data("combine_data/all_combined.json")

score_map = estimate_features(data_strings, negative_words, positive_words)
p_n_map = positive_negative_map(score_map)
generic_pie_plot(p_n_map, num_shown=3, include_others=False)

