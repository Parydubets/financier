""" The ORM models file """
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class User(UserMixin, db.Model):
    id          = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email       = db.Column(db.String(100), unique=True)
    name        = db.Column(db.String(1000))
    given_name  = db.Column(db.String(500))
    family_name = db.Column(db.String(500))
    bank_connected = db.Column(db.String(50), default = None)
    accounts    =  db.Column(db.String(20), default = None)

class Account(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(20), nullable=False)
    client_id   = db.Column(db.Integer, nullable=False)
    balance     = db.Column(db.Integer)
    limit       = db.Column(db.Integer, default = 0)

class Transaction(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    account     = db.Column(db.Integer())
    type        = db.Column(db.String(8))
    category    = db.Column(db.String(50))
    time        = db.Column(db.String(20))
    comment     = db.Column(db.String(100))
    sum         = db.Column(db.Integer)
