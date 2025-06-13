import tweepy

CONSUMER_KEY = "alfyJdUcIlMnvb7OqkKjdjHNg"
CONSUMER_SECRET = "deosRj169fPXm8vE2C4b8GezLoq5odXv8JFwf0qguF3mVu7uHD"
ACCESS_TOKEN = "1834926730945155072-7W9cJT1xpzOjEaREMAX1Ngd6HDwCO1"
ACCESS_TOKEN_SECRET = "6tkbH7zeOjvkyluN4sL2PDYivW5LWljgOAJcEXQvEX6jq"

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOGe0QEAAAAA09QZig1C34Kp5eHGE%2BH3XS2o1K4%3DhJolcJ7y1agsBhSuDEFJFcRtPFvu4D5HbTrYdNnItrZksg2mKg"

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
