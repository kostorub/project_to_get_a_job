# -*- coding: utf-8 -*-
from time import time

from aiohttp import web
from aiohttp.web import json_response

from settings import routetable, open_weather_config
from utilities.aiohttp_tools import request_session
from utilities.logging_tools import log


@routetable.get("/weather/get_weather")
async def get_weather(request):
    t_s = time()

    url_data = request.query

    town_name = url_data.get("town_name", None)

    if not isinstance(town_name, str):
        await log(
            request=request,
            time=time() - t_s,
            code=400
        )
        raise web.HTTPBadRequest()

    open_weather_request = f"https://api.openweathermap.org/data/2.5/weather?q=" \
        f"{town_name}" \
        f"&APPID=" \
        f"{open_weather_config['api_key']}" \
        f"&units=" \
        f"{open_weather_config['units']}"

    weather_data = {}
    async with request_session.get(open_weather_request) as resp:
        if resp.status == 500:
            await log(
                request=request,
                time=time() - t_s,
                code=503
            )
            raise web.HTTPServiceUnavailable()
        elif resp.status == 404:
            await log(
                request=request,
                time=time() - t_s,
                code=400
            )
            raise web.HTTPBadRequest()
        else:
            weather_data = await resp.json()

    temp = weather_data.get("main", {}).get("temp", 0.0)

    result = {
        "town": town_name,
        "temp": temp,
        "units": "metric"
    }

    await log(
        request=request,
        result=result,
        time=time() - t_s,
        code=200
    )

    return json_response(result)
