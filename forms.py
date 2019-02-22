from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional

class AddNewPetForm(FlaskForm):
    '''Form to add new pet'''
    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Pet Species', validators=[InputRequired()])
    photo_url = StringField('Pet photo URL', validators=[InputRequired()])
    age = IntegerField("Pet's age", validators=[InputRequired()])
    notes = TextAreaField("Notes about the pet:")
    available =BooleanField("Available?",validators=[InputRequired()])

    