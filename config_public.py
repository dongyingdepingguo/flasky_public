# !/usr/bin/env python

# _*_ coding: utf-8 _*_


import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '***********'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX = 'Flasky'
    FLASKY_MAIL_SENDER = '*********@qq.com'
    FLASKY_POSTS_PER_PAGE = 3


class DevelopmentConfig(Config):
    DEBUG = True
    FLASKY_ADMIN = Config.FLASKY_MAIL_SENDER
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 123
    MAIL_USE_TLS = True
    MAIL_USERNAME = '*********@qq.com'
    MAIL_RECEIVER = '*********@qq.com'
    MAIL_PASSWORD = '*********'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:*********@127.0.0.1/test_flask'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:*********@127.0.0.1/test_flask'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = None


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
