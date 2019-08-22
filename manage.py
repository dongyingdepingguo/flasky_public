#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 13:25
# @Author  : zhangshaobin
# @Site    : 
# @File    : manage.py
# @Software: PyCharm

from app import create_app, db
from flask_script import Manager, Shell

app = create_app('default')
# manager = Manager(app)
#
#
# def make_shell_context():
#     return dict(app=app)
#
#
# manager.add_command('shell', Shell(make_context=make_shell_context))
if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()
