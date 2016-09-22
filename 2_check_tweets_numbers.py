import twitter, json
def load_data(filename):
    f = open(filename,'r', encoding='utf-8').read()
    content_json = json.loads(f)
    return content_json

#Data collection Between Sept 16, 09:00-10:00 EST
content_json09_10 = load_data('combined_9_10_0916.json')

#Data collection Between Sept 16, 10:00-11:00 EST
content_json10_11 = load_data('combined_10_11_0916.json')

#Data collection Between Sept 16, 12:00-13:00 EST
content_json12_13 = load_data('combined_12_1_0916.json')


content_json_all = load_data('combined_all.json')


print("# of Tweets between Sept 16, 09:00-10:00 EST: ", len(content_json09_10))
print("# of Tweets between Sept 16, 10:00-11:00 EST: ", len(content_json10_11))
print("# of Tweets between Sept 16, 12:00-13:00 EST: ", len(content_json12_13))
print("Total # of Tweets: " ,len(content_json_all))