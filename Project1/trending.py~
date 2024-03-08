import tweepy


# Authenticate to Twitter
consumer_key = "ApPHYjEZqQRUttOZ31O1n0fRx"
consumer_secret = "VMcLhJAvjJgFYWYfEKiQWelpKxSGDRM2EzMIDZwV2FdOG7tAf7"
access_token = "102588195-xY0HTCFZ1ZTnoY5pP1YhhLHzHAMpVkFUMU5YWI9f"
access_token_secret = "rvUbjlthxbMWm47zCpfYs086qAPJQLSHP1RgAMApJ2jV8"


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
