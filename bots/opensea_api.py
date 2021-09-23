# -*- coding: utf-8 -*-

#####################################################
# OpenSea recent sales pot
# python port from 0xEssential's JS version
# https://github.com/0xEssential/opensea-discord-bot
# OpenSea docs: https://docs.opensea.io/reference/retrieving-asset-events
#####################################################

# imports
import requests 
import datetime 
import os

from dotenv import load_dotenv

load_dotenv()

# globals
COLLECTION_SLUG = os.getenv('COLLECTION_SLUG')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
OPENSEA_SHARED_STOREFRONT_ADDRESS = os.getenv('OPENSEA_SHARED_STOREFRONT_ADDRESS')

# classes

# functions
def get_opensea_recent_events():
    seconds = 3600
    hour_ago = int(datetime.datetime.now().timestamp()) - seconds # in the last hour, run hourly?

    url_search_params = {
        'offset' : '0',
        'event_type' : 'successful', # successful sales
        'only_opensea' : 'true', # only OpenSea sales
        'occurred_after' : hour_ago, 
        'collection_slug' : COLLECTION_SLUG,
    }

    if((CONTRACT_ADDRESS != OPENSEA_SHARED_STOREFRONT_ADDRESS) & (CONTRACT_ADDRESS != None)):
        url_search_params['asset_contract_address'] = CONTRACT_ADDRESS

    response = requests.get('https://api.opensea.io/api/v1/events?', params=url_search_params)
       
    return response.json()


def construct_message(item):
    message_params = {
        'buyer_name' : item.get('winner_account').get('user').get('username', "Unknown"),
        'seller_name' : item.get('seller').get('user').get('username', "Unknown"),
        'asset_name' : item.get('asset').get('name'),
        'symbol' : item.get('payment_token').get('symbol'),
        'eth_price' : float(item.get('total_price'))/10**18,
        'usd_price' : float(item.get('payment_token').get('usd_price')) * (float(item.get('total_price'))/10**18),
        'img_url' : item.get('asset').get('image_original_url'),
        'permalink' : item.get('asset').get('permalink'),
        'asset_symbol' : item.get('asset').get('asset_contract').get('asset_symbol', ''),
        'twitter_username' : item.get('asset').get('collection').get('twitter_username', ''),
    }
    
    message = (f"{message_params['buyer_name']} has bought {message_params['asset_name']} "
               f"from {message_params['seller_name']} for $ETH {message_params['eth_price']:.2f} "
               f"(USD {message_params['usd_price']:.2f}) \n #{message_params['asset_symbol']}"
               f" \n \n "
               f"{message_params['permalink']}")
    
    return message