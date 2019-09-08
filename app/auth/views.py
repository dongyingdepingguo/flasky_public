# !/usr/bin/env python

# _*_ coding: utf-8 _*_

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegistrationForm, ChangePassword, ConfirmEmail, ResetPassword, ChangeEmail
from . .model import User
from . import auth
from app import db
from . .email import send_email

@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed and request.endpoint[:5] != 'auth.':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))  ### 看不懂
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
        flash('A Confirmation email has been sent to you by email.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
        and not current_user.confirmed \
        and request.endpoint[:5] != 'auth.' \
        and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account', 'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email')
    return redirect(url_for('main.index'))


@auth.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePassword()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.new_password.data
            db.session.add(current_user)
            db.session.commit()
            flash('Your password has been changed')
            return redirect(url_for('main.index'))
        else:
            flash('Old password was entered incorrectly, please enter again!')
    return render_template('auth/change_password.html', form=form)


@auth.route('/confirm_email', methods=['GET', 'POST'])
def confirm_email():
    form = ConfirmEmail()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first() ###### 无法获取username
        if user is not None:
            token = user.generate_confirmation_token()
            send_email(email, 'Confirm Your Email', 'auth/email/confirm_email', user=user.username, token=token)
            flash('Email has been send')
            return redirect(url_for('main.index'))
        else:
            flash('Email does not exist!')
    return render_template('auth/confirm_email.html', form=form)


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    form = ResetPassword()
    if form.validate_on_submit():
        id = User().generate_confirmation_info(token=token)['id']
        if id == -1:
            flash('invalid')
            return redirect(url_for('auth.confirm_email'))
        user = User.query.filter_by(id=id).first()
        if user is not None:
            user.password = form.new_password.data
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('User does not exist!')
    return render_template('auth/reset_password.html', form=form)


@auth.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email():
    form = ChangeEmail()
    if form.validate_on_submit():
        email = current_user.email
        old_email = form.old_email.data
        new_email = form.new_email.data
        if email == old_email:
            token = current_user.generate_confirmation_token(email=new_email)
            send_email(new_email, 'Confirm New Email', 'auth/email/confirm_change_email', user=current_user, token=token)
            flash('确认邮件已发送，请注意查收！')
        else:
            flash('原始邮箱输入有误，请重新输入！')
    return render_template('auth/change_email.html', form=form)


@auth.route('/confirm_new_email/<token>', methods=['GET', 'POST'])
@login_required
def confirm_new_email(token):

    new_email = User().generate_confirmation_info(token=token)['email']
    current_user.email = new_email
    db.session.add(current_user)
    db.session.commit()
    flash('邮箱已更改！')
    return redirect(url_for('auth.change_email'))

