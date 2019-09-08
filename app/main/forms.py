#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 15:16
# @Author  : zhangshaobin
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import Form as FlaskForm
from flask_pagedown.fields import PageDownField
from . .model import Role, User


class NameForm(FlaskForm):
    name = StringField('你叫啥名？', validators=[DataRequired()])
    submit = SubmitField('提交')


class EditProfileForm(FlaskForm):
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')


class EditProfileAdminForm(FlaskForm):
    email = StringField('邮件', validators=[DataRequired(), Length(0, 64), Email()])
    username = StringField('用户名', validators=[DataRequired(),
                                                Length(1, 64),
                                                Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, numbers, '
                                                          'dots or underscores')])
    confirmed = BooleanField('确认')
    role = SelectField('角色', coerce=int)
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('地点', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.rolename) for role in Role.query.order_by(Role.rolename).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(FlaskForm):
    body = PageDownField('撰写文章', validators=[DataRequired()])
    submit = SubmitField('提交')
