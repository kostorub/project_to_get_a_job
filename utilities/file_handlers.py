# -*- coding: utf-8 -*-
import json

from utilities.exceptions import NoConfigFile


def read_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        raise NoConfigFile("No config file found!"
                           "Check it please. Doesn't work without it.")