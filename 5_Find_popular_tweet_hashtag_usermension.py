from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
from collections import OrderedDict
import string
from prettytable import PrettyTable

# Define words we do not want to show in frequent list
def unwanted():
    unwanted = list(stopwords.words('english'))
    unwanted += list(string.punctuation)
    unwanted += ['https', 'http', '...', '…',"''",'``','iphone', 'Iphone', 'iphone7', 'Iphone7',"'s"]
    return unwanted 

# Find the most frequent n words in tweets json data
def frequent_words(data, n):
    unwanted_words = unwanted()
    counts = dict() # {"word1": 253, "word2": 13}
    for tweet in data:
        if "text" in tweet.keys() and tweet["lang"]=="en":
            sentence = tweet["text"]
            words = word_tokenize(sentence)
            for word in words:
                if word.lower() not in unwanted_words:
                    counts[word] = counts.get(word, 0)+1
    sorted_counts = sorted(counts.items(), key=lambda t: t[1], reverse = True)
    with open("frequency.txt", 'w', encoding='utf-8') as f:
        f.write(str(sorted_counts[:n]))
    return sorted_counts[:n]

# Find tweets retweeted more than n times
def popular_tweet(statuses, n):
    popular = []
    for tweet in statuses:
        if "retweet_count" in tweet.keys() and tweet["retweet_count"] > n:
            popular.append(tweet)
    return popular

# Find tweets with an overall retweeted numbers more than n times
def popular_retweeted_count(statuses, n):
    popular = {}
    for tweet in statuses:
        if "retweeted_status" in tweet.keys() and len(tweet["retweeted_status"])!=0 and tweet["lang"] == "en" \
            and "retweet_count" in tweet["retweeted_status"].keys():
                if tweet["retweeted_status"]["retweet_count"] > n and "text" in tweet.keys() and len(tweet["text"])!=0:
                    if tweet["text"] not in popular.values(): 
                        popular[tweet["retweeted_status"]["retweet_count"]] = tweet["text"]
    sorted_popular = sorted(popular.items(), key=lambda t: t[0], reverse = True)
    return sorted_popular



tweets_all = load_data("combined_all.json")
frequent_words_tweets_all = frequent_words(tweets_all, 30)

# print out results as table
pt_word_frequency = PrettyTable(field_names = ['Words', 'Frequency'])
[pt_word_frequency.add_row(row) for row in frequent_words_tweets_all]
print(pt_word_frequency)

# find tweets with an overall retweeted number greater than 5000
popular_retweeted_count = popular_retweeted_count(content, 5000)
for tweet in sorted(popular_retweeted_count, reverse=True):
    print("retweeted_number: ", tweet[0], "\t","tweet_text: ", tweet[1])

    