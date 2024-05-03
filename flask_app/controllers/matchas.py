from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.matcha import Matcha
from flask_app.models.review import Review
from flask_app.models.bag import Bag
from flask import flash

# ======================= HOME PAGE ========================


@app.route('/home')
def home_page():
    if 'user_id' not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect('/')
    user = User.get_by_id(session["user_id"])
    matchas = Matcha.get_all_matchas()
    review = Review.get_all_reviews()
    bag = Bag.get_items_in_bag()
    return render_template('home.html',bag = bag, user = user, matchas=matchas, review =review)

@app.route('/about')
def about_page():
    user = User.get_by_id(session["user_id"])
    return render_template('about.html', user = user)

@app.route('/faq')
def faq_page():
    user = User.get_by_id(session["user_id"])
    return render_template('faq.html', user = user)



@app.route('/matchas')
def matchas_page():
    user = User.get_by_id(session["user_id"])
    matchas = Matcha.get_regular_matchas()
    all_matchas = Matcha.get_all_matchas()
    review = Review.get_all_reviews()
    bag = Bag.get_items_in_bag()
    return render_template('matcha.html',all_matchas=all_matchas,bag =bag, user=user, matchas= matchas, review = review)

@app.route('/recipes')
def recipes_page():
    user = User.get_by_id(session["user_id"])
    return render_template('recipes.html', user=user)

@app.route('/organic')
def organic_page():
    user = User.get_by_id(session["user_id"])
    matchas = Matcha.get_organic_matchas()
    all_matchas = Matcha.get_all_matchas()
    review = Review.get_all_reviews()
    return render_template('organic.html',all_matchas= all_matchas, user=user, matchas =matchas, review=review)


@app.route("/quiz")
def quiz():
    pass
    # quiz_dict = Matcha.start_quiz(user_input)
    # return render_template('quiz.html', quiz_dict = quiz_dict)