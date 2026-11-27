from flask import Flask, render_template

app = Flask(__name__)
from db import db

@app.route('/')
def index():
    return render_template('Startseite.html')

@app.route('/guides')
def guides(): 
    return render_template('Studienguides.html')

@app.route('/profile')
def profile():
    return render_templat('Profil.html')