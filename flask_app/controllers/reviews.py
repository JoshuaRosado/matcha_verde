from flask import Flask, render_template, redirect, session, request
from flask_app import app
app.secret_key = "Waves are breaking izquierda"
from flask_app.models.user import User
from flask_app.models.matcha import Matcha
from flask_app.models.review import Review
from flask import flash


# ======================= HOME PAGE ========================


# ======================= VIEW ITEM ========================

@app.route('/leave_review/<matcha_name>')
def leave_review(matcha_name):
    reviews = Review.get_all_reviews()
    matchas = Matcha.get_matcha_name(matcha_name)
    user = User.get_by_id(session["user_id"])
    return render_template('leave_review.html', user=user, matchas=matchas, reviews=reviews)


@app.route('/create_review', methods = ["POST"])
def create_review():
    valid_review = Review.leave_a_review(request.form)
    if valid_review:
        return redirect('/home')
    return redirect('/faq')


@app.route('/item/<matcha_name>')
def item_page(matcha_name):
    user = User.get_by_id(session['user_id'])
    reviews = Review.get_all_reviews()
    review = Review.get_matcha_user_review(matcha_name)
    return render_template('item.html', user=user,review=review,reviews=reviews)

