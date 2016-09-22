from nltk.tokenize import word_tokenize
import json
from nltk.corpus import twitter_samples, stopwords
import string
from TwitterPlot import generic_pie_plot, number_bar_plot
import matplotlib.pyplot as plt
%pylab inline

def load_data(filename):
    f = open(filename,'r', encoding='utf-8').read()
    content_json = json.loads(f)
    return content_json

def estimate_keyword_features(data, keywords_lst, negative_words, positive_words):
	data_strings = []
	for tweet in data:
		if "lang" in tweet.keys() and tweet["lang"]=="en" and "text" in tweet.keys() and len(tweet["text"])!=0:
			to_be_added = ""
			for keyword in keywords_lst:
				if keyword.lower() in tweet['text'].lower() and tweet["text"]!= to_be_added:
					to_be_added = tweet["text"]
			if to_be_added != "":
				data_strings.append(to_be_added)
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

def positive_negative_plot(lst, title):
	p_n_map = {"positive":0, "negative":0, "neutral":0}
	for pair in lst:
		if pair[0]>0:
			p_n_map["positive"] += pair[1]
		elif pair[0] == 0:
			p_n_map["neutral"] += pair[1]
		else:
			p_n_map["negative"] += pair[1]
	generic_pie_plot(p_n_map, num_shown=3, include_others=False, title=title)

negative_words = load_data("negative_words_cleaned.json")
positive_words = load_data("positive_words_cleaned.json")
data_strings = load_data("combined_all.json")
query_jetblack = ["jet black", "jet", "black"]
query_earphone = ["earphone", "ear phone", "headphone", "lightning", "3.5"]
query_waterproof = ["water", "waterproof", "swim"]
query_camera = ["camera", "double", "dual", "zoom"]


camera = estimate_keyword_features(data_strings, query_camera, negative_words, positive_words)
positive_negative_plot(camera, title="Camera")

earphone = estimate_keyword_features(data_strings, query_earphone, negative_words, positive_words)
positive_negative_plot(earphone, title="Earphone")

waterproof = estimate_keyword_features(data_strings, query_waterproof, negative_words, positive_words)
positive_negative_plot(waterproof, title="Waterproof")

jetblack = estimate_keyword_features(data_strings, query_jetblack, negative_words, positive_words)
positive_negative_plot(jetblack, title="Jetblack")