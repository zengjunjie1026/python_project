#!/usr/bin/env python3
# encoding: utf-8

'''
@author: zengjunjie
@contact: zengjunjie@thinkenergy.tech
@software: Pycharm
@application:
@file: log.py
@time: 09/06/22 18:15
@desc:
'''
from logging.config import dictConfig
from example_blog.config import settings


def init_log():
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'sample': {'format': '%(asctime)s %(levelname)s %(message)s'},
            'verbose': {'format': '%(asctime)s %(levelname)s %(name)s %(process)d %(thread)d %(message)s'},
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
            },
        },
        'handlers': {
            "console": {
                "formatter": 'verbose',
                'level': 'DEBUG',
                "class": "logging.StreamHandler",
            },
        },
        'loggers': {
            '': {'level': settings.LOG_LEVEL, 'handlers': ['console']},
        },
    }

    dictConfig(log_config)
