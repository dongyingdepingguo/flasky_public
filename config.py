#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 13:22
# @Author  : zhangshaobin
# @Site    :
# @File    : config.py
# @Software: PyCharm

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX = 'Flasky'
    FLASKY_MAIL_SENDER = '2867432325@qq.com'


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '2867432325@qq.com'
    MAIL_PASSWORD = 'yfexvjdytugzdfbf'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:31415926z@127.0.0.1/test_flask'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:31415926z@127.0.0.1/test_flask'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = None


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}