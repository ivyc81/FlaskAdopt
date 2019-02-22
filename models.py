
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


def connect_db(app):
        """ connect to db"""
        db.app = app
        db.init_app(app)


class Pet(db.Model):
    '''Pet class '''
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
