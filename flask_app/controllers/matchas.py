from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.matcha import Matcha
from flask import flash

# ======================= HOME PAGE ========================

@app.route('/home')
def home():
    if 'user_id' not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect('/')
    user = User.get_by_id(session["user_id"])
    matchas = Matcha.get_all()
    return render_template('home.html', user = user, matchas=matchas)
        
@app.route('/about')
def about():
    user = User.get_by_id(session["user_id"])
    return render_template('about.html', user = user)

@app.route('/faq')
def faq():
    user = User.get_by_id(session["user_id"])
    return render_template('faq.html', user = user)