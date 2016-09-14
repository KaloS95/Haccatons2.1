# -*- coding: utf-8 -*-

from app import app
from flask import render_template, redirect, session

from .forms import *

from utils import *

def login_required(func):
    def func_wrapper(*args, **kwargs):
        if not session.get('user', None):
            return redirect('/login')
        return func(*args, **kwargs)
    return func_wrapper

@app.route('/')
def index():
    if not session.get('user', None):
        return redirect('/login')
    return redirect('/offer/category')

@app.route('/<mode>/category/')
@login_required
def category_list(mode):
    context = getCategoryList()
    return render_template('category.html',
                            context=context)

@app.route('/<mode>/category/<category_id>/')
@login_required
def category_detail(mode,category_id):
    context = getItemFromCategory(category_id)
    return render_template('items_list.html',
			    context=context)

@app.route('/<mode>/category/<category_name>/<item_id>/', methods=["GET", "POST"])
@login_required
def items_list_form_category(mode,category_name, item_id):
    if mode == 'offer':
        form = NewOfferForm()
        context = getItemFromId(item_id)
        context['form'] = form
        if form.validate_on_submit():
            create_offer(form, context['item'])
            return redirect('/offer-created')
        return render_template('create_offer.html', context=context)
    elif mode == 'search':
        context = getItemOffers(item_id)
        return render_template('offers_list.html',
                    context=context)
    else:
        return redirect('/')

@app.route('/<mode>/category/<category_name>/<item_id>/<order_id>', methods=["GET", "POST"])
@login_required
def order_detail(mode,category_name, item_id, order_id):
    form = OfferForm()

    if form.validate_on_submit():
        session['quantity'] = form.quantity.data
        return redirect('/request-success/' + order_id + "/")
    context = getOrderDetail(order_id)
    context['form'] = form
    return render_template('offer_detail.html',
                           context=context)

@app.route('/<mode>/request-success/<order_id>/')
@login_required
def request_success(mode, order_id):
    context = getOrderDetail(order_id)
    create_transition(context['order'])
    return render_template('request-success.html', context=context)

"""
USER LOGGING
"""
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
@login_required
def logout_user():
    logout()
    return redirect('/') 
