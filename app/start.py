from aiohttp import web
import aiohttp_jinja2
import jinja2

from config.urls import urls


def add_urls(app):
    for url in urls:
        app.add_routes(url)
    
        

def start_app():
    app = web.Application()
    aiohttp_jinja2.setup(app, 
                        loader=jinja2.FileSystemLoader('templates'))
    app.add_routes([web.static('/static', 'static')])
    app['static_root_url'] = '/static'
    add_urls(app)
    web.run_app(app)


if __name__ == "__main__":
    start_app()