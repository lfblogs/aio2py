#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 3.4.x
# Last Modified: 2015/7/16 17:21


__all__ = []
__author__ = "lfblogs (email:13701242710@163.com)"
__version__ = "1.0.1"


import asyncio
import aiomysql
import logging

logging.basicConfig(level=logging.INFO)

@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('Create database connection pool...')
    global __pool
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