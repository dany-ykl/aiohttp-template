from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    login = Column(String(50), primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return f"{self.login}:{self.name}"

#Base.metadata.create_all(engine)

