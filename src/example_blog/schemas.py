#!/usr/bin/env python3
# encoding: utf-8

'''
@author: zengjunjie
@contact: zengjunjie@thinkenergy.tech
@software: Pycharm
@application:
@file: schemas.py.py
@time: 09/06/22 18:24
@desc:
'''

from datetime import datetime
from typing import Optional, TypeVar
from pydantic import BaseModel, constr
from example_blog.models import BaseModel as DBModel

ModelType = TypeVar('ModelType', bound=DBModel)
CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)


class InDBMixin(BaseModel):
    id: int

    class Config:
        orm_mode = True


class BaseArticle(BaseModel):
    title: constr(max_length=500)
    body: Optional[str] = None


class ArticleSchema(BaseArticle, InDBMixin):
    create_time: datetime
    update_time: datetime


class CreateArticleSchema(BaseArticle):
    pass


class UpdateArticleSchema(BaseArticle):
    title: Optional[constr(max_length=500)] = None

