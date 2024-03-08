import tweepy

# Authenticate to Twitter

# Authenticate to Twitter
consumer_key = "ApPHYjEZqQRUttOZ31O1n0fRx"
consumer_secret = "VMcLhJAvjJgFYWYfEKiQWelpKxSGDRM2EzMIDZwV2FdOG7tAf7"
access_token = "102588195-xY0HTCFZ1ZTnoY5pP1YhhLHzHAMpVkFUMU5YWI9f"
access_token_secret = "rvUbjlthxbMWm47zCpfYs086qAPJQLSHP1RgAMApJ2jV8"


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
