import json
from prettytable import PrettyTable


def load_data(filename):
	f = open(filename,'r', encoding='utf-8').read()
	content_json = json.loads(f)
	return content_json

def setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids):
    
    friends_ids, followers_ids = set(friends_ids), set(followers_ids)
    
    print('{0} is following {1}'.format(screen_name, len(friends_ids)))

    print('{0} is being followed by {1}'.format(screen_name, len(followers_ids)))
    
    print('{0} of {1} are not following {2} back'.format(
            len(friends_ids.difference(followers_ids)), 
            len(friends_ids), screen_name))
    
    print('{0} of {1} are not being followed back by {2}'.format(
            len(followers_ids.difference(friends_ids)), 
            len(followers_ids), screen_name))
    
    print('{0} has {1} mutual friends'.format(
            screen_name, len(friends_ids.intersection(followers_ids))))



friends = load_data("cook_friends_info.json")
followers = load_data("cook_followers_info.json")
print(len(friends))
print(len(followers))

friends_ids_names = [   (friend[0]['id'], friend[0]["screen_name"])
                        for friend in friends[:20]  ]

followers_ids_names = [ (follower[0]['id'], follower[0]["screen_name"])
                        for follower in followers[:20]  ]

pt_friends = PrettyTable(field_names = ['friend_id', 'friend_name'])
[ pt_friends.add_row(row) for row in friends_ids_names]
pt_followers = PrettyTable(field_names = ['follower_id', 'follower_name'])
[ pt_followers.add_row(row) for row in followers_ids_names]

print(pt_friends)
print(pt_followers)

screen_name = "tim_cook"
friends_ids = [	friend[0]['id'] for friend in friends ]
followers_ids = [ follower[0]['id'] for follower in followers ]

setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids)

