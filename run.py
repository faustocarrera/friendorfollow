#!/usr/bin/python
# -*- coding: utf-8 -*-
"Run Mirtha, run..."

import os
import click
import tweepy
from helper import Config

__version__ = '0.1.0'
__updated__ = '2018-03-19'


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
    twitter_api = setup_tweepy(config.get_twitter())
    ctx.obj['twitter'] = None


@run.command()
@click.pass_context
def following(ctx):
    "The people you follow not following you"
    pass


if __name__ == '__main__':
    run(obj={})
