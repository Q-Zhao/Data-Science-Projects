# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import time
import datetime
from time import mktime
import json

def load_data(filename):
	f = open(filename,'r', encoding='utf-8').read()
	content_json = json.loads(f)
	return content_json


def plot_hist_time_tweets_num(data):
	start_time = datetime.datetime.strptime(data[0]["created_at"], "%a %b %d %H:%M:%S +0000 %Y")
	start_point = unixTime = mktime(start_time.timetuple())
	time_counter = {}
	for tweet in data:
		# Example: "Fri Sep 16 13:28:59 +0000 2016"
		if "created_at" in tweet.keys():
			time_str = tweet["created_at"]
			time_formated = datetime.datetime.strptime(time_str, "%a %b %d %H:%M:%S +0000 %Y")
			unixTime = mktime(time_formated.timetuple())
			time_counter[unixTime-start_point] = time_counter.get(unixTime, 0)+1
	time_counter = sorted(time_counter.items(), key=lambda t: t[0])
	x, y = [], []
	for couple in time_counter:
		x.append(couple[0])
		y.append(couple[1])
	bins = []
	for i in range(400):
		bins.append(i*10)
	plt.hist(x, bins, histtype='bar', rwidth=0.1)
	plt.xlabel('time')
	plt.ylabel('tweets number')
	plt.title('tweets number by time')
	plt.legend()
	plt.show()

tweets_09_10 = load_data("combined_all.json")
plothist_time_tweets_num(tweets_09_10)
