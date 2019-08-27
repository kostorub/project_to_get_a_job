# -*- coding: utf-8 -*-
from settings import routetable
from aiohttp import web
from aiohttp.web import json_response


@routetable.get("/weather/get_weather")
async def get_weather(request):
    url_data = request.query

    town_name = None
    if "town_name" in url_data:
        town_name = url_data["town_name"]

    if not isinstance(town_name, str):
        raise web.HTTPBadRequest()

    result = {
        "town": town_name,
        "temp": 0.0,
        "units": "metric"
    }

    return json_response(result)
