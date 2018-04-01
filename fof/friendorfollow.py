#!/usr/env/bin python
# -*- coding: utf-8 -*-
"""
Friend or follow class
"""

import tweepy


class FriendOrFollow(object):
    "Friend or follow"

    __updated__ = '2018-01-24'
    follows = []
    nofollow = []

    def __init__(self, api):
        self.api = api
        self.me = self.myself()

    def myself(self):
        return self.api.me()

    def followers(self):
        "Get the people following me"
        followers = self.api.followers_ids(self.me.id)
        for user_id in followers:
            if user_id in self.follows:
                # remove from list
                self.follows.remove(user_id)

    def following(self):
        "Get the people I follow"
        followings = self.api.friends_ids(self.me.id)
        for user_id in followings:
            self.follows.append(user_id)

    def nofriends(self):
        "Get the people I follow not following me"
        for user_id in self.follows:
            self.nofollow.append(self.api.get_user(user_id))

    def result(self):
        self.following()
        self.followers()
        self.nofriends()
        return self.nofollow
