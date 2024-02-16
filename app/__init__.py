from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL', 'sqlite:///data.db')

db = SQLAlchemy(app)

from .routes import *  # Importa as rotas depois de inicializar app e db

def create_tables():
    db.create_all()
