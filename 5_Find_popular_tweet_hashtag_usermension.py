import twitter
import sys
import io
import json
import os
from prettytable import PrettyTable

def load_data(filename):
    f = open(filename,'r', encoding='utf-8').read()
    content_json = json.loads(f)
    return content_json

def count_tweet_hashtags_user_mentions(statuses):
    hashtags, user_mentions= {}, {}
    for tweet in statuses:
        if "entities" in tweet.keys() and len(tweet["entities"])!=0:
            if "hashtags" in tweet["entities"] and len(tweet["entities"]["hashtags"])!=0:
                for hashtag in tweet["entities"]["hashtags"]:
                    hashtags[hashtag["text"]] = hashtags.get(hashtag["text"], 0)+1          
            if "user_mentions" in tweet["entities"] and len(tweet["entities"]["user_mentions"])!=0:
                for user_mension in tweet["entities"]["user_mentions"]:
                    user_mentions[user_mension['screen_name']] = user_mentions.get(user_mension['screen_name'],0)+1
    top_10_hashtags = sorted(hashtags.items(), key=lambda t: t[1], reverse=True)[:10]
    top_10_user_mentions = sorted(user_mentions.items(), key=lambda t: t[1], reverse=True)[:10]
    return top_10_hashtags, top_10_user_mentions



content = load_data('combined_9_10_0916.json')
hashtags, user_mentions = count_tweet_hashtags_user_mentions(content)

pt_hashtags = PrettyTable(field_names = ['Top 10 hashtags', 'hashtags #'])
[ pt_hashtags.add_row(row) for row in hashtags]
pt_user_mentions = PrettyTable(field_names = ['Top 10 user_mentions', 'user_mentions #'])
[ pt_user_mentions.add_row(row) for row in user_mentions]

print(pt_hashtags)
print(pt_user_mentions)

