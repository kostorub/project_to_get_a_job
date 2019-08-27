# -*- coding: utf-8 -*-
import os

from aiohttp import web

from utilities.file_handlers import read_config

routetable = web.RouteTableDef()


open_weather_config = read_config(
    os.path.join("config", "open_weather_map.json"))
