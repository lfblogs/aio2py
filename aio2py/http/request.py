# -*- coding: UTF-8 -*-

__author__ = "lfblogs"


import functools
import logging

logging.basicConfig(level=logging.INFO)

def get(path):
    '''
        Define decorator @get('/path'):
    '''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

def post(path):
    '''
        Define decorator @post('/path'):
    '''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator


