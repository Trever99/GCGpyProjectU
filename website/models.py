from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150))
    email = db.Column(db.String(160), unique=True)
    password = db.Column(db.String(150))
    
    students = db.relationship('Student')
    
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    rollnr = db.Column(db.String(5), unique=True)
    gender = db.Column(db.String(150))
    email = db.Column(db.String(160), unique=True)
    phonenr = db.Column(db.String(10), unique=True)
    age = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
