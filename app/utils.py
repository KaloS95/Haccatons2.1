from app import models, db
from flask import session
from sqlalchemy.orm.exc import NoResultFound

def login(data):
    username = data.username.data
    password = data.password.data

    try:
        user = models.User.query.filter(models.User.username==username).one()

        if (user.password == password):
            session['user'] = user.to_json()

            return True
        return False
    except NoResultFound, e:
        return False

def create_user(data):
    new_user = models.User(username=data.username.data, 
                password=data.password.data,
                phone_number=data.number.data)

    db.session.add(new_user)
    db.session.commit()

def logout():
    session['user'] = None

def getCategoryList():
    context = {}

    category = models.Category.query.all()

    context['category'] = category

    return context

def getItemList(item_id):
    context = {}

    offers = models.Offer.query.filter(models.Offer.item_id==item_id).all()

    context['offers']=offers

    return context

def getItemFromCategory(cat_id):
    context = {}
    items_list = models.Category.query.get(cat_id).items.all()
    context['items_list'] = items_list
    return context

def getItemOffers(item_id):
    context = {}

    item_offers = models.Item.query.filter(models.Item.id==item_id).one().av_offers.all()

    context['item_offers'] = item_offers
	
    return context

def getOrderDetail(order_id):
    context = {}
    order = models.Offer.query.get(order_id) 
    context['order'] = order
    return context

def create_transition(order):
    buyer = models.User.query.get(session.get('user', None)['id'])
    seller = order.offerer 
    quantity = session.get('quantity', 0)

    newTrans = models.Transition(buyer=buyer, seller=seller, order=order, quantity=quantity)

    db.session.add(newTrans)
    db.session.commit()
