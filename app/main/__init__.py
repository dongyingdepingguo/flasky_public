#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 14:27
# @Author  : zhangshaobin
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
