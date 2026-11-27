
from flask import Flask, render_template
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yuni.sqlite'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('Startseite.html')


@app.route('/guides')
def guides():
    return render_template('Studienguides.html')


@app.route('/profile')
def profile():
    return render_template('Profil.html')


@app.route('/community/forum')
def community_forum():
    return render_template('Community_forum.html')


@app.route('/community/links')
def community_links():
    return render_template('Community_links.html')


if __name__ == '__main__':
    app.run(debug=True)
