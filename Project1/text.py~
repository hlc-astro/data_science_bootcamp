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

# Fetch tweets from Elon Musk
tweets = api.user_timeline(screen_name="elonmusk", count=10)

# Print the tweets
for tweet in tweets:
    print(tweet.text)
    print("-------------")
