# -*- coding: utf-8 -*-


class NoConfigFile(Exception):
    def __init__(self, message=""):
        self.message = message
