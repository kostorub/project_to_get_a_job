# -*- coding: utf-8 -*-
from aiohttp import web
from settings import routetable

import routes.weather.get_by_town_name

app = web.Application()
app.add_routes(routetable)

web.run_app(app, host="0.0.0.0", port=7000)
