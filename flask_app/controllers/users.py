from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
# from flask_app.models.matcha import Matcha
from flask import flash

# ===================== INDEX ======================
@app.route('/')
def index():
    return render_template('index.html')

# ===================== LOGIN ======================
@app.route('/login_page')
def login_page():
    return render_template('login.html')

# ===================== LOGIN PROCESS ======================

@app.route('/login' , methods = ['POST'])
def login():
    valid_user = User.authentication_user_input(request.form)
    # If user's email is not valid
    if not valid_user:
        # Redirect the user back to login page
        return redirect("login_page")
    session['user_id'] = valid_user.id
    return redirect("/home")

# ===================== REGISTER ======================
@app.route('/register_page')
def register_page():
    return render_template('register.html')

# ===================== REGISTER PROCESS ======================

@app.route('/register', methods = ['POST'])
def register():
    valid_user = User.register_new_user(request.form)
    
    if not valid_user:
        return redirect('/register_page')
    
    session['user_id'] = valid_user.id
    return redirect('/home')

# ===================== LOGOUT======================

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
