from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.matcha import Matcha
from flask_app.models.review import Review
from flask_app.models.bag import Bag
from flask import flash


@app.route('/base')
def base():
    if 'user_id' not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect('/')
    user = User.get_by_id(session["user_id"])
    bag = Bag.add_to_bag()
    matchas = Matcha.get_all_matchas()
    review = Review.get_all_reviews()