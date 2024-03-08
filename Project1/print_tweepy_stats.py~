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
