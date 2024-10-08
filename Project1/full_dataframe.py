
'''
author: Holly L. Capelo

Program using the open source python package 'tweepy' to obtain twitter data using the API. This program will obtain the full tweet history of the specified user. Additionally statistics about each tweet and the location where the tweet occurred will be printed.

'''

import tweepy

# Authenticate to Twitter 
#Note that the AUTHENTICATION data is not shared and the credentials for an active account should be put in place. 

# Authenticate to Twitter
consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Specify the username of the user you want to retrieve the tweet history for
#username = "elonmusk"
username="richardbranson"

# Fetch the user's tweet history
tweets = api.user_timeline(screen_name=username, count=200, tweet_mode="extended")

# Initialize a list to store the extracted tweet data
tweet_data = []

# Process each tweet in the tweet history
for tweet in tweets:
    # Extract basic tweet information
    tweet_info = {
        
        "created_at": tweet.created_at,
        "text": tweet.full_text,
        "retweet_count": tweet.retweet_count,
        "favorite_count": tweet.favorite_count,
        "hashtags": [hashtag["text"] for hashtag in tweet.entities["hashtags"]],
        "mentions": [mention["screen_name"] for mention in tweet.entities["user_mentions"]]
    }
    
    # Extract geolocation if available
    if tweet.place is not None and tweet.place.bounding_box is not None:
        coordinates = tweet.place.bounding_box.coordinates[0]
        latitude = (coordinates[0][1] + coordinates[2][1]) / 2
        longitude = (coordinates[0][0] + coordinates[2][0]) / 2
        tweet_info["latitude"] = latitude
        tweet_info["longitude"] = longitude
    
    # Append tweet data to the list
    tweet_data.append(tweet_info)

# Print the extracted tweet data
for tweet in tweet_data:
    print(tweet)
    print("--------------")
