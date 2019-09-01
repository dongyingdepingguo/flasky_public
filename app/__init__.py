#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 13:21
# @Author  : zhangshaobin
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


from flask import Flask, request, redirect, render_template, url_for, session, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Message, Mail
from flask_login import LoginManager
from flask_moment import Moment
from config import config


bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
login_manger = LoginManager()
login_manger.session_protection = 'strong'
login_manger.login_view = 'auth.login'
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    login_manger.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.app_context().push()

    return app