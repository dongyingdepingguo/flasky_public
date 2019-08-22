#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 15:16
# @Author  : zhangshaobin
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class NameForm(FlaskForm):
    name = StringField('你叫啥名？', validators=[DataRequired()])
    submit = SubmitField('提交')
