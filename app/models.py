from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    phone_number = db.Column(db.Integer)
    auth_code = db.Column(db.String(5))

    def __repr__(self):
        return "<User: %r>" % self.username

    def to_json(self):
        return {
            "username": self.username,
            "phone_number": self.phone_number
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return "<Category: %r>" % self.name

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Transition(db.Model):
    id = db.Column(db.Integer, primary_key=True)

