# -*- coding: utf-8 -*-
import aiohttp
import aiosqlite

from utilities.sql_queries import create_table_logging_query

# Session for the requests to the weather provider
request_session = aiohttp.ClientSession()


async def init_db_connection(app):
    db = await aiosqlite.connect("sqlite.db")
    app["engine"] = db
    await db.execute(create_table_logging_query)


async def close_aiohttp_sessions(app):
    await request_session.close()
    await app["engine"].close()
