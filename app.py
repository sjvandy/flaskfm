from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET KEY'] = 'all-hail-the-magic-conch'

db = SQLAlchemy

@app.route('/')
@app.route('/index')
def greeting():
    return render_template('greeting.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

