import tweepy
import configparser

api_key = ""
api_key_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)
