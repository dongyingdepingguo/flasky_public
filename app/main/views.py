#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 14:37
# @Author  : zhangshaobin
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from flask import redirect, render_template, url_for, session
from datetime import datetime

from . import main
from .forms import NameForm
from app import db
from app.model import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
    return render_template('index.html', current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False))




