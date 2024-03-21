from typing import TYPE_CHECKING
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./song_library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'all-hail-the-magic-conch'
db.init_app(app)

from models import User, Song, Playlist, Item
if TYPE_CHECKING: # Adds autocomplete to SQL-Alchemy
    from flask_sqlalchemy.model import Model

    BaseModel = db.make_declarative_base(Model)

@app.route('/')
@app.route('/index')
def greeting():
    return render_template('greeting.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

import routes