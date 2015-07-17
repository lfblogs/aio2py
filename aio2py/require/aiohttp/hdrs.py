"""HTTP Headers constants."""
from aio2py.require.aiohttp.multidict import upstr

METH_ANY = upstr('*')
METH_CONNECT = upstr('CONNECT')
METH_HEAD = upstr('HEAD')
METH_GET = upstr('GET')
METH_DELETE = upstr('DELETE')
METH_OPTIONS = upstr('OPTIONS')
METH_PATCH = upstr('PATCH')
METH_POST = upstr('POST')
METH_PUT = upstr('PUT')
METH_TRACE = upstr('TRACE')

ACCEPT = upstr('ACCEPT')
ACCEPT_CHARSET = upstr('ACCEPT-CHARSET')
ACCEPT_ENCODING = upstr('ACCEPT-ENCODING')
ACCEPT_LANGUAGE = upstr('ACCEPT-LANGUAGE')
ACCEPT_RANGES = upstr('ACCEPT-RANGES')
ACCESS_CONTROL_MAX_AGE = upstr('ACCESS-CONTROL-MAX-AGE')
ACCESS_CONTROL_ALLOW_CREDENTIALS = upstr('ACCESS-CONTROL-ALLOW-CREDENTIALS')
ACCESS_CONTROL_ALLOW_HEADERS = upstr('ACCESS-CONTROL-ALLOW-HEADERS')
ACCESS_CONTROL_ALLOW_METHODS = upstr('ACCESS-CONTROL-ALLOW-METHODS')
ACCESS_CONTROL_ALLOW_ORIGIN = upstr('ACCESS-CONTROL-ALLOW-ORIGIN')
ACCESS_CONTROL_REQUEST_HEADERS = upstr('ACCESS-CONTROL-REQUEST-HEADERS')
AGE = upstr('AGE')
ALLOW = upstr('ALLOW')
AUTHORIZATION = upstr('AUTHORIZATION')
CACHE_CONTROL = upstr('CACHE-CONTROL')
CONNECTION = upstr('CONNECTION')
CONTENT_DISPOSITION = upstr('CONTENT-DISPOSITION')
CONTENT_ENCODING = upstr('CONTENT-ENCODING')
CONTENT_LANGUAGE = upstr('CONTENT-LANGUAGE')
CONTENT_LENGTH = upstr('CONTENT-LENGTH')
CONTENT_LOCATION = upstr('CONTENT-LOCATION')
CONTENT_MD5 = upstr('CONTENT-MD5')
CONTENT_RANGE = upstr('CONTENT-RANGE')
CONTENT_TRANSFER_ENCODING = upstr('CONTENT-TRANSFER-ENCODING')
CONTENT_TYPE = upstr('CONTENT-TYPE')
COOKIE = upstr('COOKIE')
DATE = upstr('DATE')
DESTINATION = upstr('DESTINATION')
DIGEST = upstr('DIGEST')
ETAG = upstr('ETAG')
EXPECT = upstr('EXPECT')
EXPIRES = upstr('EXPIRES')
FROM = upstr('FROM')
HOST = upstr('HOST')
IF_MATCH = upstr('IF-MATCH')
IF_MODIFIED_SINCE = upstr('IF-MODIFIED-SINCE')
IF_NONE_MATCH = upstr('IF-NONE-MATCH')
IF_RANGE = upstr('IF-RANGE')
IF_UNMODIFIED_SINCE = upstr('IF-UNMODIFIED-SINCE')
KEEP_ALIVE = upstr('KEEP-ALIVE')
LAST_EVENT_ID = upstr('LAST-EVENT-ID')
LAST_MODIFIED = upstr('LAST-MODIFIED')
LINK = upstr('LINK')
LOCATION = upstr('LOCATION')
MAX_FORWARDS = upstr('MAX-FORWARDS')
ORIGIN = upstr('ORIGIN')
PRAGMA = upstr('PRAGMA')
PROXY_AUTHENTICATE = upstr('PROXY_AUTHENTICATE')
PROXY_AUTHORIZATION = upstr('PROXY-AUTHORIZATION')
RANGE = upstr('RANGE')
REFERER = upstr('REFERER')
RETRY_AFTER = upstr('RETRY-AFTER')
SEC_WEBSOCKET_ACCEPT = upstr('SEC-WEBSOCKET-ACCEPT')
SEC_WEBSOCKET_VERSION = upstr('SEC-WEBSOCKET-VERSION')
SEC_WEBSOCKET_PROTOCOL = upstr('SEC-WEBSOCKET-PROTOCOL')
SEC_WEBSOCKET_KEY = upstr('SEC-WEBSOCKET-KEY')
SEC_WEBSOCKET_KEY1 = upstr('SEC-WEBSOCKET-KEY1')
SERVER = upstr('SERVER')
SET_COOKIE = upstr('SET-COOKIE')
TE = upstr('TE')
TRAILER = upstr('TRAILER')
TRANSFER_ENCODING = upstr('TRANSFER-ENCODING')
UPGRADE = upstr('UPGRADE')
WEBSOCKET = upstr('WEBSOCKET')
URI = upstr('URI')
USER_AGENT = upstr('USER-AGENT')
VARY = upstr('VARY')
VIA = upstr('VIA')
WANT_DIGEST = upstr('WANT-DIGEST')
WARNING = upstr('WARNING')
WWW_AUTHENTICATE = upstr('WWW-AUTHENTICATE')
