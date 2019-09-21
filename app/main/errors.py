#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 14:37
# @Author  : zhangshaobin
# @Site    : 
# @File    : errors.py
# @Software: PyCharm

from flask import render_template
from app import db
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    db.session.commit()
    return render_template('500.html'), 500


@main.app_errorhandler(403)
def user_no_permission(e):
    return render_template('500.html'), 403