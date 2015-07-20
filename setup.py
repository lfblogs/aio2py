from distutils.core import setup

setup(
    name='aio2py',
    version='1.1.6',
    packages=['aio2py', 'aio2py.db', 'aio2py.api', 'aio2py.app', 'aio2py.conf', 'aio2py.http', 'aio2py.utils',
              'aio2py.required', 'aio2py.required.aiopg', 'aio2py.required.aiopg.sa', 'aio2py.required.aiohttp',
              'aio2py.required.aiomysql', 'aio2py.required.aiomysql.sa'],
    url='http://github.com/lfblogs',
    license='GUN Linense',
    author='Liu Fei',
    author_email='13701242710@163.com',
    description='Simple web Frame'
)
