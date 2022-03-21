from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE = {'db':
           {   'ENGINE':'postgresql',
               'HOST': 'localhost',
               'DATABASE': 'aiohttp_test2',
               'USER': 'aiohttp_user',
               'PASSWORD': 'Ckjdfhm123!',
               'PORT': '5432'
           }
        }
