# -*- coding: utf-8 -*-

from app import app
from flask import render_template, redirect, session

from .forms import LoginForm, RegisterForm 

from utils import create_user, login, logout, getCategoryList

@app.route('/')
def index():
    if not session['user']:
        return redirect('/login')
    return redirect('/category')

@app.route('/category')
def category_list():
    context = getCategoryList()
    return render_template('category.html',
                            context=context)

@app.route('/category/<category_name>/')
def category_detail(category_name):
    return category_name

@app.route('/category/<category_name>/<item_id>/')
def items_list_form_category(category_name, item_id):
    return "Category: %s Id: %s" % (category_name, item_id)
    

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
