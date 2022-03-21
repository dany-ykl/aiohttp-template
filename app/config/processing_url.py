import importlib

from aiohttp import web


class PathUrl:

    def __init__(self, path):
        self.check_tuple(path)
        
    def check_tuple(self, tuple):
        self.method = tuple[0]
        self.url = tuple[1]
        self.view = tuple[2]
        try:
            self.name = tuple[3]
        except IndexError:
            self.name = None

def path_url(path:str):
    urls = []
    module = importlib.import_module(path)
    for i in module.urls:
        path = PathUrl(i)
        if path.method == 'get':
            urls.append(web.get(path.url, path.view, name=path.name))
        if path.method == 'post':
            urls.append(web.post(path.url, path.view, name=path.name))
        if path.method == 'put':
            urls.append(web.put(path.url, path.view, name=path.name))
        if path.method == 'patch':
            urls.append(web.patch(path.url, path.view, name=path.name))
            
    return urls