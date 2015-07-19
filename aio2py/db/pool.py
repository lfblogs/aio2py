# -*- coding: UTF-8 -*-

__author__ = "Liu Fei"
__github__ = "http://github.com/lfblogs"
__all__ = [
    "Pool"
]

"""

Define database connection pool

"""


import asyncio
import logging
try:
    import aiomysql
except ImportError:
    from aio2py.required import aiomysql

try:
    import aiopg
except ImportError:
    from aio2py.required import aiopg

logging.basicConfig(level=logging.INFO)


@asyncio.coroutine
def Pool(loop,**kw):
    logging.info('Create database connection pool...')
    global __pool
    ENGINE = kw.get('ENGINE',None)
    if not ENGINE:
        raise KeyError('Not found database ENGINE in conf files...')
    if ENGINE == 'mysql':
        __pool = yield from aiomysql.create_pool(
        host = kw.get('host', ''),
        port = kw.get('port', 3306),
        user = kw.get('user', ''),
        password = kw.get('password', ''),
        db = kw.get('db', ''),
        charset = kw.get('charset', 'utf8'),
        autocommit = kw.get('autocommit', True),
        maxsize = kw.get('maxsize', 10),
        minsize = kw.get('minsize', 1),
        loop = loop
        )
    elif ENGINE == 'postgresql':

        __pool = yield from aiopg.pool.create_pool(
        host = kw.get('host', ''),
        port = kw.get('port', 5432),
        user = kw.get('user', ''),
        password = kw.get('password', ''),
        database = kw.get('db', ''),
        maxsize = kw.get('maxsize', 10),
        minsize = kw.get('minsize', 1),
        loop = loop
        )
    else:
        raise KeyError('Database ENGINE Error...')