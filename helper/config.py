#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Handle the configuration file
"""

import configparser


class Config(object):
    "Class to handle the configuration files"

    config_data = {}

    def __init__(self, config_file):
        self.read_config(config_file)

    def read_config(self, config_file):
        "load config file and parse the content"
        config_parser = configparser.RawConfigParser()
        config_parser.read(config_file)
        # twitter
        self.config_data['consumer'] = {
            'key': config_parser.get('consumer', 'key'),
            'secret': config_parser.get('consumer', 'secret')
        }
        self.config_data['access'] = {
            'token': config_parser.get('access', 'token'),
            'secret': config_parser.get('access', 'secret')
        }

    def configuration(self):
        "return config data"
        return self.config_data

    def __get_config(self, key):
        "return config data"
        if key in self.config_data:
            return self.config_data[key]
        return None

    def get_consumer(self):
        "return consumer config"
        return self.__get_config('consumer')

    def get_access(self):
        "return access config"
        return self.__get_config('access')

    def get_twitter(self):
        "return full twitter data"
        return {
            'consumer': self.__get_config('consumer'),
            'access': self.__get_config('access')
        }
