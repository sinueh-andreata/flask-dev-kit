from config import app, db
from flask import render_template, jsonify

@app.route('/login_page')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

