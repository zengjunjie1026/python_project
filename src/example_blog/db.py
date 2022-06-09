#!/usr/bin/env python3
# encoding: utf-8

'''
@author: zengjunjie
@contact: zengjunjie@thinkenergy.tech
@software: Pycharm
@application:
@file: db.py
@time: 09/06/22 18:23
@desc:
'''
"""Database connections"""

from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from example_blog.config import settings

url = URL(
    drivername=settings.DATABASE.DRIVER,
    username=settings.DATABASE.get('USERNAME', None),
    password=settings.DATABASE.get('PASSWORD', None),
    host=settings.DATABASE.get('HOST', None),
    port=settings.DATABASE.get('PORT', None),
    database=settings.DATABASE.get('NAME', None),
    query=settings.DATABASE.get('QUERY', None),
)

engine: Engine = create_engine(url, echo=True)

SessionFactory = sessionmaker(bind=engine, autocommit=False, autoflush=True)

ScopedSession = scoped_session(SessionFactory)
