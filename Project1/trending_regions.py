'''
author: Holly L. Capelo

Program using the open source python package 'tweepy' to obtain twitter data using the API. This program can be used to obtain and report worldwide trends in specified regions. 
'''


import tweepy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np


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

# Define the WOEID values and region keys
regions = {
    "Worldwide": 1,
    "United States": 23424977,
    "United Kingdom": 23424975,
    "Canada": 23424775,
    "Australia": 23424748,
    "India": 23424848,
    "Switzerland": 783058,
    "Germany": 638242
}

# Retrieve the top trending hashtags for each region
for region, woeid in regions.items():
    # Retrieve the trending topics for the specified location
    trends = api.get_place_trends(id=woeid)

    print(f"Trending Hashtags in {region}:")
    for trend in trends[0]["trends"]:
        if trend["name"].startswith("#"):
            hashtag = trend["name"]
            tweet_volume = trend.get("tweet_volume", 0) or 0
            print(f"{hashtag}: {tweet_volume}")

    print()

