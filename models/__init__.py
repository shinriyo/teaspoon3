# -*- coding: utf-8 -*-
"""
this sets up sqlalchemy.
for more information about sqlalchemy check out <a href="http://www.sqlalchemy.org/">www.sqlalchemy.org</a>
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# inherit DeclarativeBase class when you write up a model.
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata

# set the connection string here
#the good postgresql module
engine = create_engine('postgresql+psycopg2://teaspoon:teaspoon@localhost/teaspoon')
#it also can use
#engine = create_engine('sqlite+pysqlite:///file.db')

Session = sessionmaker(bind=engine, autocommit=True)

# import the dbsession instance to execute queries on your database
dbsession = Session()

# import your models.
from models.auth import Group, Permission, User

# calling this will create the tables at the database
__create__ = lambda: (setattr(engine, 'echo', True), metadata.create_all(engine))
