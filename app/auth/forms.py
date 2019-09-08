# !/usr/bin/env python

# _*_ coding: utf-8 _*_

from wtforms import Form as FlaskForm
from wtforms import SubmitField, PasswordField, BooleanField, StringField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from . .model import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, numbers, '
                                                          'dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')


class ChangePassword(FlaskForm):
    old_password = PasswordField('old password', validators=[DataRequired()])
    new_password = PasswordField('new password', validators=[DataRequired()])
    new_password2 = PasswordField('confirm new password', validators=[DataRequired(),
                                                                      EqualTo('new_password',
                                                                              message='Passwords must match')])
    submit = SubmitField('Confirm Change')


class ConfirmEmail(FlaskForm):
    email = StringField('Your Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Confirm Send')


class ResetPassword(FlaskForm):
    new_password = PasswordField('new_password', validators=[DataRequired()])
    confirm_new_password = PasswordField('confirm_new_password', validators=[DataRequired(),
                                                                             EqualTo('new_password',
                                                                                     message='Passwords must match')])
    submit = SubmitField('Confirm Reset')


class ChangeEmail(FlaskForm):
    old_email = StringField('old email', validators=[DataRequired(), Length(1, 64), Email()])
    new_email = StringField('new email', validators=[DataRequired(), Length(1, 64), Email()])
    confirm_new_email = StringField('confirm new email', validators=[DataRequired(), EqualTo('new_email',
                                                                                             message='Email must match')])
    submit = SubmitField('Confirm Change Email')
