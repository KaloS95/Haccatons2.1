from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    phone_number = db.Column(db.Integer)
    auth_code = db.Column(db.String(5))

    def __repr__(self):
        return "<User: %r>" % self.username

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Transition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
