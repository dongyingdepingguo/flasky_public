# !/usr/bin/env python

# _*_ coding: utf-8 _*_

from flask import current_app, render_template
from flask_mail import Message
from app import mail


def send_email(to, subject, template, **kwargs):
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=current_app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    # msg.html = render_template(template + '.html', **kwargs)
    msg.body = render_template(template + '.txt', **kwargs)
    mail.send(msg)