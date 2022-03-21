from curses import echo
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel, root_validator

from .settings import DATABASE
 

class InfoDatabase(BaseModel):
    ENGINE: str
    HOST: str
    DATABASE: str
    USER: str
    PASSWORD: str
    PORT: str
 
class Database(BaseModel):
    db: InfoDatabase

    @root_validator(skip_on_failure=True)
    def check_id(cls, values):
        db: InfoDatabase = values.get('db')
        return values
                  

db = Database(**DATABASE)

engine = create_engine(f'postgresql+psycopg2://{db.db.USER}:'\
f'{db.db.PASSWORD}@{db.db.HOST}:{db.db.PORT}/{db.db.DATABASE}', echo=True)

session = sessionmaker(bind=engine)()
