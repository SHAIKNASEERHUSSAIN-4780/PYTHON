import tweepy

CONSUMER_KEY = "provide your consumer key"
CONSUMER_SECRET = "provide your consumer secret"
ACCESS_TOKEN = "provide your access token"
ACCESS_TOKEN_SECRET = "provide your access token secret"

BEARER_TOKEN = "provide your bearer token"

def OAuthVerifier():
    auth = tweepy.OAuth1UserHandler(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)
    return api

def get_bearer_token():
    return BEARER_TOKEN
