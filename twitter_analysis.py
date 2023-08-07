import pandas as pd
import tweepy
from configparser import ConfigParser

# read configs
config = ConfigParser()
config.read('config.ini')

api_key = config["twitter"]["api_key"]
api_key_secret = config["twitter"]["api_key_secret"]
access_token = config["twitter"]["access_token"]
access_token_secret = config["twitter"]["access_token_secret"]

# authentication
auth = tweepy.OAuth2AppHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# user = api.verify_credentials()
# print(f'Authenticated user: {user.screen_name}')

search_query = "bitcoin"
# search for tweets
tweets = api.search_tweets(q=search_query, lang="en", count=10)
# print results
for tweet in tweets: # Causes error. Need v2 access endpoints.
    print(f"User: {tweet.user.screen_name}")
    print(f"Tweet: {tweet.text}")
    print("---")

# # scraping
# keywords = "bitcoin"
# cursor = tweepy.Cursor(api.search_tweets, q="bitcoin",
#                        lang="en", tweet_mode="extended").items(5)
# text_tweets = [[tweet.text] for tweet in cursor]
# print(text_tweets)
