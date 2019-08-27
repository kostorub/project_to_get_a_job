# -*- coding: utf-8 -*-


create_table_logging_query =\
    """CREATE TABLE IF NOT EXISTS logging (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        request TEXT NOT NULL,
        response TEXT NOT NULL,
        request_time TEXT NOT NULL,
        response_time TEXT NOT NULL,
        response_code INTEGER NOT NULL
    );"""

logging_insert =\
    """INSERT INTO logging
    (request, response, request_time, response_time)
    VALUES
    (%s, %s, %s, %s)
    """
