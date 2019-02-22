from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class AddNewPetForm(FlaskForm):
    '''Form to add new pet'''
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Pet Species', choices=[('dog','dog'), ('cat','cat'), ('porcupine','porcupine')], validators=[InputRequired()])
    photo_url = StringField('Pet photo URL', validators=[Optional(), URL()])
    age = IntegerField("Pet's age", validators=[NumberRange(min=0, max=30), InputRequired()])
    notes = TextAreaField("Notes about the pet:")
    available = BooleanField("Available?")


class EditPetForm(FlaskForm):
    """Form to edit pet"""

    photo_url = StringField('Pet photo URL', validators=[InputRequired()])
    notes = TextAreaField("Notes about the pet:")
    available = BooleanField("Available?")
