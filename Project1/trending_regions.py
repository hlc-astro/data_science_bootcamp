import tweepy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np


# Authenticate to Twitter
consumer_key = "ApPHYjEZqQRUttOZ31O1n0fRx"
consumer_secret = "VMcLhJAvjJgFYWYfEKiQWelpKxSGDRM2EzMIDZwV2FdOG7tAf7"
access_token = "102588195-xY0HTCFZ1ZTnoY5pP1YhhLHzHAMpVkFUMU5YWI9f"
access_token_secret = "rvUbjlthxbMWm47zCpfYs086qAPJQLSHP1RgAMApJ2jV8"



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

