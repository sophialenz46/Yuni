import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yuni.sqlite'

db = SQLAlchemy()
db.init_app(app)

#Tabelle Beitrag 
class Beitrag(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    kategorie = db.Column(db.String(200))
    text = db.Column(db.Text)

#Tabelle Antwort  
class Antwort(db.Model):
     id = db.Column(db.Integer, primary_key=True)


#Tabelle Kategorie
class Kategorie(db.Model):
 id = db.Column(db.Integer, primary_key=True)

#Tabellen erstellen     
with app.app_context():
    db.create_all()