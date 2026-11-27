import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from datetime import datetime

db = SQLAlchemy()

#Tabelle Beitrag 
class Beitrag(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    kategorie_id = db.Column(db.Integer, db.ForeignKey('kategorie.id'),nullable=False)
    text = db.Column(db.Text, nullable=False)
    erstellt_am = db.Column(db.DateTime, default=datetime.now, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#Tabelle Antwort  
class Antwort(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     text = db.Column(db.Text, nullable=False)
     erstellt_am = db.Column(db.DateTime, default=datetime.now, nullable=False)
     beitrag_id = db.Column(db.Integer, db.ForeignKey('beitrag.id'), nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#Tabelle GruppenLink
class GruppenLink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    link = db.Column(db.String(200), nullable=False, unique=True)
    kategorie_id = db.Column(db.Integer, db.ForeignKey('kategorie.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#Tabelle Kategorie
class Kategorie(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String(200), nullable=False, unique=True)


 #Tabelle Studiengang
class Studiengang(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False, unique=True)


#Tabelle Modul
class Modul(db.Model): 
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False)
    studiengang_id = db.Column(db.Integer, db.ForeignKey('studiengang.id'), nullable=False)


#Tabelle User    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    passwort_hash = db.Column(db.String(200), nullable=False) 
    hochschule = db.Column(db.String(200), nullable=False, default='HWR Berlin')
    studiengang_id = db.Column(db.Integer, db.ForeignKey('studiengang.id'), nullable=False) 
    erstellt_am = db.Column(db.DateTime, nullable=False, default=datetime.now, nullable=False)                  

 

#Tabelle Guide
#class Guide(db.Model):
#   id = db.Column(db.Integer, primary_key=True, index=True)
#    phase = db.Column(db.String, nullable=False)
#    titel = db.Column(db.String, nullable=False, unique = True)
#   beschreibung = db.Column(db.String, nullable=False)


#Tabellen erstellen     (muss immer ganz unten als letztes stehen!)
#with app.app_context():
#    db.create_all()