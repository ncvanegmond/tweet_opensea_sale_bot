# -*- coding: utf-8 -*-
# https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials
import logging
import os

import tweepy
from dotenv import load_dotenv

logger = logging.getLogger()
load_dotenv()

def create_api():
    consumer_key = os.getenv("API_KEY")
    consumer_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

if __name__ == "__main__":
    print('main')
