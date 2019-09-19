#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 13:25
# @Author  : zhangshaobin
# @Site    : 
# @File    : manage.py
# @Software: PyCharm

from app import create_app, db
from app.model import User, Role, Post
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, user=User, role=Role, post=Post)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
