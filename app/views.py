# -*- coding: utf-8 -*-

from app import app
from flask import render_template, redirect, session

from .forms import *

from utils import *

@app.route('/')
def index():
    if not session.get('user', None):
        return redirect('/login')
    return redirect('/category')

@app.route('/category/')
def category_list():
    context = getCategoryList()
    return render_template('category.html',
                            context=context)

@app.route('/category/<category_id>/')
def category_detail(category_id):
    context = getItemFromCategory(category_id)
    return render_template('items_list.html',
			    context=context)

@app.route('/category/<category_name>/<item_id>/')
def items_list_form_category(category_name, item_id):
    context = getItemOffers(item_id)
    return render_template('offers_list.html',
			    context=context)

@app.route('/category/<category_name>/<item_id>/<order_id>', methods=["GET", "POST"])
def order_detail(category_name, item_id, order_id):
    form = OfferForm()

    if form.validate_on_submit():
        session['quantity'] = form.quantity.data
        return redirect('/request-success/' + order_id + "/")
    context = getOrderDetail(order_id)
    context['form'] = form
    return render_template('offer_detail.html',
                           context=context)

@app.route('/request-success/<order_id>/')
def request_success(order_id):
    context = getOrderDetail(order_id)
    create_transition(context['order'])
    return render_template('request-success.html', context=context)

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
