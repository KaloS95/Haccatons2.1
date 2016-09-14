from app import db
from sqlalchemy import and_, or_

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    phone_number = db.Column(db.Integer)
    auth_code = db.Column(db.String(5))

    offers = db.relationship('Offer', backref='offerer', lazy="dynamic")

    db.relationship('Transition', backref="buyer", lazy="dynamic") 
    db.relationship('Transition', backref="seller", lazy="dynamic") 

    def __repr__(self):
        return "<User: %r>" % self.username

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "phone_number": self.phone_number
        }
    def getTransition(self, isInProgress):
        if isInProgress:
            return Transition.query.filter(and_(Transition.concluded == False, Transition.seller_id == self.id)).all()
        else:
            return Transition.query.filter(and_(Transition.concluded == True, Transition.seller_id == self.id)).all()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20)) 
    items = db.relationship('Item', backref='category', lazy="dynamic")

    def __repr__(self):
        return "<Category: %r>" % self.name

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64))
    category_id=db.Column(db.Integer, db.ForeignKey('category.id'))
    av_offers = db.relationship('Offer', backref='item', lazy="dynamic")

class Transition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    quantity = db.Column(db.Integer)

    buyer = db.relationship('User', backref="transitions_as_buyer", foreign_keys=[buyer_id])
    seller = db.relationship('User', backref="transitions_as_seller", foreign_keys=[seller_id])
    order = db.relationship('Offer', backref="transitions", foreign_keys=[order_id])

    concluded = db.Column(db.Boolean)

    def __init__(self, **kwargs):
        super(Transition, self).__init__(**kwargs)
        self.concluded = False
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<%r -> %r = %r>" % (self.buyer.username, self.seller.username, self.quantity)

class Offer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    item_id=db.Column(db.Integer, db.ForeignKey('item.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    quantity=db.Column(db.Integer)
    price=db.Column(db.Integer)

    db.relationship('Transition', backref="order")
    user = db.relationship('User', backref="user", foreign_keys=[user_id])
    
  
