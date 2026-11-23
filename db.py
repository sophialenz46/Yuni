import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yuni.sqlite'

db = SQLAlchemy()
db.init_app(app)