# -*- coding: utf-8 -*-
import json
from datetime import datetime

import pytz

from utilities.sql_queries import logging_insert


async def log(*args, **kwargs):
    """
    Logging data in sqlite
    :param args:
    :param kwargs:
    request - request to the route
    result - dict with answer to the client
    time - processing time
    code - http response code
    :return:
    """
    request = kwargs.get("request", None)
    if request is None:
        return
    result = kwargs.get("result", {})
    processing_time = kwargs.get("time", 0)
    code = kwargs.get("code", 200)
    await request.app["engine"].execute(
        logging_insert,
        (
            str(request.url),
            json.dumps(result),
            str(datetime.now(tz=pytz.UTC)),
            str(processing_time),
            int(code)
        )
    )
    await request.app["engine"].commit()
