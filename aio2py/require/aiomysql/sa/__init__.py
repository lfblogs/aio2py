"""Optional support for sqlalchemy.sql dynamic query generation."""
from aio2py.require.aiomysql.sa.connection import SAConnection
from aio2py.require.aiomysql.sa.engine import create_engine, Engine
from aio2py.require.aiomysql.sa.exc import (Error, ArgumentError, InvalidRequestError,
                  NoSuchColumnError, ResourceClosedError)


__all__ = ('create_engine', 'SAConnection', 'Error',
           'ArgumentError', 'InvalidRequestError', 'NoSuchColumnError',
           'ResourceClosedError', 'Engine')


(SAConnection, Error, ArgumentError, InvalidRequestError,
 NoSuchColumnError, ResourceClosedError, create_engine, Engine)
