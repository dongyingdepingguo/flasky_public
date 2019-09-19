#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 14:27
# @Author  : zhangshaobin
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
from . .model import Permission

main = Blueprint('main', __name__)

from . import views, errors


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)