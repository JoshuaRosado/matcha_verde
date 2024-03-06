from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.matcha import Matcha
from flask_app.models.review import Review
from flask import flash


# ======================= HOME PAGE ========================


# ======================= VIEW ITEM ========================

@app.route('/see_review/<int:review_id>')
def see_review(review_id, matcha_name):
    review = Review.get_by_id(review_id)
    matchas = Matcha.get_matcha_name(matcha_name)
    user = User.get_by_id(session["user_id"])
    return render_template('see_review.html', review=review, user=user, matchas = matchas)


@app.route('/leave_review', methods = ['POST'])
def leave_review_page():
    valid_review = Review.leave_a_review(request.form)
    if valid_review:
        return redirect(f'/home')
    return redirect('/leave_review')




@app.route('/item/<matcha_name>')
def matchas_page(matcha_name):
    review = Review.get_all_reviews()
    user = User.get_all()
    matcha = Matcha.get_matcha_name(matcha_name)
    return render_template('matcha.html', user=user)