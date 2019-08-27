# -*- coding: utf-8 -*-
import aiohttp


request_session = aiohttp.ClientSession()


async def close_aiohttp_sessions():
    await request_session.close()
