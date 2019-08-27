# -*- coding: utf-8 -*-
import aiohttp


request_session = aiohttp.ClientSession()


async def close_aiohttp_sessions(app):
    await request_session.close()
