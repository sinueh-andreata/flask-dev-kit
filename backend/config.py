from flask import Flask, app
from sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
app = Flask(__name__, template_folder=TEMPLATE_DIR)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = False  # True em produção com HTTPS
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///root:password@localhost:3306/db_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16 MB
db = SQLAlchemy(app)