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
