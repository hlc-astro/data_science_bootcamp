
'''
author: Holly L. Capelo

Program using the open source python package 'tweepy' to obtain twitter data using the API. This program can be used to obtain and report worldwide trends. Should be modified to report arbitrary region from user prompt (currently set to only global).  

'''


import tweepy


# Authenticate to Twitter
consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Prompt the user to enter the location (WOEID) for trending topics
woeid = input("Enter the WOEID for the location (1 for worldwide): ")

if woeid == "1":
    woeid = 1

# Retrieve the trending topics for the specified location
#trends = api.trends_place(woeid)

# Retrieve the trending topics for the specified location
trends = api.get_place_trends(id=woeid)

# Extract the trending hashtags
trending_hashtags = []
for trend in trends[0]["trends"]:
    if trend["name"].startswith("#"):
        trending_hashtags.append(trend["name"])

# Print the trending hashtags
print("Trending Hashtags:")
for hashtag in trending_hashtags:
    print(hashtag)
