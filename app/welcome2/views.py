from aiohttp import web


async def index(request):
    return web.Response(text='2Welcome!')

async def index2(request):
    return web.Response(text='2Welcome2!')