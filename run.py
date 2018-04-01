#!/usr/bin/python
# -*- coding: utf-8 -*-
"Run Mirtha, run..."

import os
import click
import tweepy
from helper import Config
from fof import FriendOrFollow

__version__ = '0.1.0'
__updated__ = '2018-04-01'


def get_config(file_path):
    "Get config data"
    config_path = os.path.realpath(file_path)
    return Config(config_path)


def setup_tweepy(twitter):
    "setup twitter"
    auth = tweepy.OAuthHandler(
        twitter['consumer']['key'],
        twitter['consumer']['secret']
    )
    auth.set_access_token(
        twitter['access']['token'],
        twitter['access']['secret']
    )
    return tweepy.API(auth)


def get_path(filename):
    "Return file real path"
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


@click.group()
@click.pass_context
def run(ctx):
    config_file = get_path('config/app.conf')
    config = get_config(config_file)
    ctx.obj['twitter_api'] = setup_tweepy(config.get_twitter())


@run.command()
@click.pass_context
def fof(ctx):
    "Friend or follow list"
    twitter_api = ctx.obj['twitter_api']
    friendorfollow = FriendOrFollow(twitter_api)
    nofollow = friendorfollow.result()
    for user in nofollow:
        print('http://twitter.com/{0}'.format(user.screen_name))


if __name__ == '__main__':
    run(obj={})
