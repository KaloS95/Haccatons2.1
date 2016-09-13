# -*- coding: utf-8 -*-

from app import app
from flask import render_template, redirect

from .forms import LoginForm, RegisterForm 

from utils import create_user, login, logout

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        # No errors! We can proceed!
        create_user(register_form)
        return redirect('/index') 
    return render_template('register.html', form=register_form)

@app.route('/login', methods=["GET", "POST"])
def login_user():
    form = LoginForm()

    if form.validate_on_submit():
        if login(form):
            return redirect('/index')
        return redirect('/login')
    return render_template('login.html',
                           form=form)

@app.route('/logout')
def logout_user():
    logout()
    return redirect('/') 
