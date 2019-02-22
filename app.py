from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

from datetime import datetime
from flask_wtf import FlaskForm
from forms import AddNewPetForm
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

#route to homepage
@app.route('/')
def list_of_pets():
    '''display list of pets'''
    pets = Pet.query.all()


    return render_template('homepage.html', pets=pets)

@app.route('/add',methods=["GET", "POST"])
def add_new_pet():
    ''' Form to add new pet'''
    form = AddNewPetForm()

    if form.validate_on_submit():
        # import pdb
        # pdb.set_trace()
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name = name, species = species, photo_url= photo_url, age = age, notes = notes, available = available)
        db.session.add(new_pet)
        db.session.commit()
        
        #return f"Add {name} at {price}"
        # redirect("/")
        return redirect('/')

    else:
        return render_template("pet_add_form.html", form=form)





    
