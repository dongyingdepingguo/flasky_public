#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 16:10
# @Author  : zhangshaobin
# @Site    : 
# @File    : model.py
# @Software: PyCharm

from . import db


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(32), unique=True)
    user = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(32), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    password_hash = db.Column(db.String(128))
