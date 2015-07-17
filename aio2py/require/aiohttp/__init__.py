# This relies on each of the submodules having an __all__ variable.

__version__ = '0.16.5'

from aio2py.require.aiohttp.protocol import *  # noqa
from aio2py.require.aiohttp.connector import *  # noqa
from aio2py.require.aiohttp.client import *  # noqa
from aio2py.require.aiohttp.errors import *  # noqa
from aio2py.require.aiohttp.helpers import *  # noqa
from aio2py.require.aiohttp.parsers import *  # noqa
from aio2py.require.aiohttp.streams import *  # noqa
from aio2py.require.aiohttp.multidict import *  # noqa
from aio2py.require.aiohttp.multipart import *  # noqa
from aio2py.require.aiohttp.websocket_client import *  # noqa


__all__ = (client.__all__ +
           errors.__all__ +
           helpers.__all__ +
           parsers.__all__ +
           protocol.__all__ +
           connector.__all__ +
           streams.__all__ +
           multidict.__all__ +
           multipart.__all__ +
           websocket_client.__all__ +
           ('hdrs', '__version__'))
