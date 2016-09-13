# -*- coding: utf-8 -*-

from app import app, models, db
from flask import render_template, redirect

from sqlalchemy.orm.exc import NoResultFound

from .forms import LoginForm, RegisterForm 

def authenticate_user(form):
    username = form.username.data
    password = form.password.data

    try:
        user = models.User.query.filter(models.User.username==username).one()

        if (user.password == password):
            return True
        return False
    except NoResultFound, e:
        return False

def create_user(form):
    new_user = models.User(username=form.username.data, 
                password=form.password.data,
                phone_number=form.number.data)

    db.session.add(new_user)
    db.session.commit()

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
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if authenticate_user(form):
            return redirect('/index')
        return redirect('/login')
    return render_template('login.html',
                           form=form)
