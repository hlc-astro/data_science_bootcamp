'''
author: Holly L. Capelo

Program using the open source python package 'tweepy' to obtain twitter data using the API. This program will obtain basic statistics for a specified user's account.

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

# Prompt the user to enter the Twitter username
username = input("Enter the Twitter username: ")

# Fetch the user's information
user = api.get_user(screen_name=username)

# Retrieve user's attributes
tweet_count = user.statuses_count
follower_count = user.followers_count
friend_count = user.friends_count
favorite_count = user.favourites_count

# Print user's information
print("Username:", username)
print("Tweets since their first tweet:", tweet_count)
print("Followers:", follower_count)
print("Friends:", friend_count)
print("Favorites (Likes):", favorite_count)
