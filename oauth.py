#!/usr/bin/python

"""
OAuth script
Me: Just give me permission to publish tweets!
Twitter API: OK!
"""

import sys
import os
import configparser
import tweepy


def setup_config():
    "help setup the config file"
    script_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_path, 'config/app.conf')
    # check if file exists
    if not os.path.isfile(filename):
        sys.exit('Error: you have to create the config file')
    # load configuration
    config_parser = configparser.RawConfigParser()
    config_parser.read(filename)
    # config
    config = {
        'consumer_key': config_parser.get('consumer', 'key'),
        'consumer_secret': config_parser.get('consumer', 'secret'),
        'access_token': config_parser.get('access', 'token'),
        'access_secret': config_parser.get('access', 'secret'),
    }
    return config


def run():
    config = setup_config()
    auth = tweepy.OAuthHandler(
        config['consumer_key'], config['consumer_secret'])

    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        sys.exit('Error! Failed to get request token.')
    # verify
    print('Please, go to %s to verify' % redirect_url)
    verifier = input('Verifier:')
    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        sys.exit('Error! Failed to get access token.')
    # the keys
    print('Access data')
    print('token: %s' % auth.access_token)
    print('secret: %s' % auth.access_token_secret)
    sys.exit('bye!')


if __name__ == '__main__':
    run()
