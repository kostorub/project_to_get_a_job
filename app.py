# -*- coding: utf-8 -*-
from aiohttp import web
from settings import routetable

import routes.weather.get_by_town_name
from utilities.aiohttp_tools import close_aiohttp_sessions, init_db_connection

app = web.Application()
app.add_routes(routetable)

app.on_startup.append(init_db_connection)
app.on_cleanup.append(close_aiohttp_sessions)

web.run_app(app, host="0.0.0.0", port=7000)
