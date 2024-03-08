
'''
author: Holly L. Capelo

Program using the open source python package 'tweepy' to obtain twitter data using the API. This program can be used to check if the connection to the API is working and obtain a few tweets from a specified user. The screen_name can be changed as wished. 

'''



import tweepy

# Authenticate to Twitter
#Note that the AUTHENTICATION data is not shared and the credentials for an active account should be put in place. 

consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Fetch tweets from Elon Musk
tweets = api.user_timeline(screen_name="elonmusk", count=10)

# Print the tweets
for tweet in tweets:
    print(tweet.text)
    print("-------------")
