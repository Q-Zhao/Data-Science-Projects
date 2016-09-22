# -*- coding: utf-8 -*-
import json
from TwitterPlot import generic_bar_plot, generic_pie_plot, number_bar_plot

locations_dict = {"United States":["USA","AL", "Alabama","AK", "Alaska","AS", "American Samoa","AZ", "Arizona","AR", "Arkansas","CA", "California","CO", "Colorado","CT", "Connecticut","DE", "Delaware","DC", "District Of Columbia","FM", "Federated States Of Micronesia","FL", "Florida","GA", "Georgia","GU", "Guam","HI", "Hawaii","ID", "Idaho","IL", "Illinois","IN", "Indiana","IA", "Iowa","KS", "Kansas","KY", "Kentucky","LA", "Louisiana","ME", "Maine","MH", "Marshall Islands","MD", "Maryland","MA", "Massachusetts","MI", "Michigan","MN", "Minnesota","MS", "Mississippi","MO", "Missouri","MT", "Montana","NE", "Nebraska","NV", "Nevada","NH", "New Hampshire","NJ", "New Jersey","NM", "New Mexico","NY", "New York","NC", "North Carolina","ND", "North Dakota","MP", "Northern Mariana Islands","OH", "Ohio","OK", "Oklahoma","OR", "Oregon","PW", "Palau","PA", "Pennsylvania","PR", "Puerto Rico","RI", "Rhode Island","SC", "South Carolina","SD", "South Dakota","TN", "Tennessee","TX", "Texas","UT", "Utah","VT", "Vermont","VI", "Virgin Islands","VA", "Virginia","WA", "Washington","WV", "West Virginia","WI", "Wisconsin","WY", "Wyoming"]}

def load_data(filename):
	f = open(filename,'r', encoding='utf-8').read()
	content_json = json.loads(f)
	return content_json

def users_created_time(data):
	users_created_time = {}
	for tweet in data:
		if "user" in tweet.keys() and "created_at" in tweet["user"].keys():
			time_str = tweet["user"]["created_at"]
			year = int(time_str.split(" ")[-1])
			users_created_time[year] = users_created_time.get(year, 0)+1
	return users_created_time

def users_locations(data):
	users_locations_mapping = {}
	for tweet in data:
		if "user" in tweet.keys() and "location" in tweet["user"].keys() \
			and tweet["user"]["location"] != None:
			# location = tweet["user"]["location"]
			location = str(tweet["user"]["location"].split(", ")[-1])
			for k, v in locations_dict.items():
				for i in v:
					if location == i:
						location = k
			users_locations_mapping[location] = users_locations_mapping.get(location, 0)+1
	return users_locations_mapping

def users_timezones(data):
	users_timezone_mapping = {}
	for tweet in data:
		if "user" in tweet.keys() and "time_zone" in tweet["user"].keys() \
			and tweet["user"]["time_zone"] != None:
			timezone = tweet["user"]["time_zone"]
			users_timezone_mapping[timezone] = users_timezone_mapping.get(timezone, 0)+1
	return users_timezone_mapping

def tweets_languages(data):
	language_mapping = {}
	for tweet in data:
		if "lang" in tweet.keys() and tweet["lang"]!= None:
			lang = tweet["lang"]
			language_mapping[lang] = language_mapping.get(lang, 0)+1
	return language_mapping


	


# tweets_09_10 = load_data("combined_9_10_0916.json")

# user_created_time = users_created_time(tweets_09_10)
# number_bar_plot(user_created_time)


# users_locations = users_locations(tweets_09_10)
# generic_bar_plot(users_locations)
# generic_pie_plot(users_locations)


# users_timezones = users_timezones(tweets_09_10)
# generic_bar_plot(users_timezones)
# generic_pie_plot(users_timezones, include_others=False)

# users_languages = tweets_languages(tweets_09_10)
# generic_bar_plot(users_languages)
# generic_pie_plot(users_languages)







