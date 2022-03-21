from aiohttp import web
from aiohttp_jinja2 import render_template
from .models import User
from config.database import session


async def index(request):
    return render_template('welcome/index.html', request, context={'s':'s'})

async def index2(request):
    return render_template('welcome/post.html', request, context=None)

async def index3(request):
    data = await request.post()
    login = data['login']
    name = data['first_name']
   
    user = User(login=login, name=name)
    session.add(user)
    session.commit()

    return render_template('welcome/post.html', request, context={'login': login, 'first_name': name})
   
    
    