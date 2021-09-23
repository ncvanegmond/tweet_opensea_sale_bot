# -*- coding: utf-8 -*-
# https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials

# import tweepy
import logging
from config import create_api
from opensea_api import get_opensea_recent_events, construct_message
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_recent_sales(api, token_id):
    logger.info("Calling OpenSea")
    dct = get_opensea_recent_events().get('asset_events')
    new_token_id = int(dct[0].get('asset').get('token_id'))
    logger.info(f"current token_id {token_id} \n  most recent token_id {new_token_id}")
    if new_token_id != token_id:
        logger.info(f"new token_id: {new_token_id}! \n Constructing message")
        message = construct_message(dct[0])
        logger.info(f"tweeting: {message}")
        api.update_status(
            status = message,
        )
    else:
        logger.info("no new sale..")

    return new_token_id

def main():
    api = create_api()
    token_id = 6590
    while True:
        token_id = check_recent_sales(api, token_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()