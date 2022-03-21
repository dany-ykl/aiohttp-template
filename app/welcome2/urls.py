from aiohttp import web

from . import views

urls = [
    ('get', '/welcome2/test', views.index),
    ('get', '/welcome2/test2', views.index2, 'w2t2')
]