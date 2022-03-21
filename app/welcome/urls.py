from aiohttp import web

from . import views

#('method', 'url', 'views', 'name')
#('get', '<name_app>/hello', views.index, 'hello'),

urls = [
    ('get', '/welcome/test', views.index, 'test'),
    ('get', '/welcome/test2', views.index2, 'test2'),
    ('post', '/welcome/test3', views.index3, 'test3'),    
]