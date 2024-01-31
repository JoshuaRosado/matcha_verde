from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import matcha
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
DB = "matcha_verde"


class User:
    
    def __init__(self, user):
        
        self.id = user["id"]
        self.first_name = user["first_name"]
        self.last_name = user["last_name"]
        self.email = user["email"]
        self.password = user["password"]
        self.created_at = user["created_at"]
        self.updated_at = user["updated_at"]
        self.matcha = []
        
    @classmethod
    # Find user by the email------
    def get_by_email(cls, email):
        # Using the email data
        data = {
            "email": email}
        # Find the user where the email matches the entered by user
        query = "SELECT * FROM users WHERE email = %(email)s;"
        # Results returns as a list from DB
        results = connectToMySQL(DB).query_db(query, data)
        
        # if the result can't be found or is less than 1
        if len(results)< 1:
            return False
        # else return the first index in the instance of the list
        return cls(results[0])
        
    @classmethod
    def get_by_id(cls, id):
        data ={
            "id":id
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        
        if len(results)< 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        
        query = "SELECT * FROM users";
        user_data = connectToMySQL(DB).query_db(query)
        
        users = []
        #  for each user in the user_data coming back from the DB
        for user in user_data:
            # Append that user cls to the users empty list
            users.append(cls(user))
        # return users list
        return users
    
    # ================ VERIFYING AUTHENTICATION ===================
    @classmethod
    def authentication_user_input(cls, user_input):
        valid = True
        valid_password = True
        existing_user = cls.get_by_email(user_input["email"])
        
        # if is not an existing user return False
        if not existing_user:
            valid = False
        #  Else proceed to the password
        else: 
            valid_password = bcrypt.check_password_hash(existing_user.password, user_input["password"])
            # If password is not valid return False
            if not valid_password:
                valid = False
        #  If valid is false flash this message
        if not valid:
            flash("Password does not match our records")
            return False
        #If everything is Valid return the existing user
        return existing_user
    
    # ================ REGISTER PROCESS ===================
    
    @classmethod
    def register_new_user(cls, user):
        
        if not cls.is_valid(user):
            return False
        
        pw_hash = bcrypt.generate_password_hash(user['password'])
        user = user.copy()
        user['password'] = pw_hash
        print("User after adding pw: ", user)
        
        query = """
                INSERT INTO users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        
        new_user_id = connectToMySQL(DB).query_db(query, user)
        new_user = cls.get_all(new_user_id)
        
        return new_user
    
# ================ VERIFYING IF IS VALID ===================
    @classmethod
    def is_valid(cls, user):
        valid = True
        #  if the length of the first name is less than 2 characters
        if len(user["first_name"]) < 2:
            # Return False and Flash message
            valid = False
            flash("First name must be at least 2 characters")
        #  if the length of the last name is less than 2 characters
        if len(user["last_name"])< 2:
            valid = False
            flash("Last name must be at least 2 characters")
        # If is the email is not properly written Flash message
        if not EMAIL_REGEX.matcha(user["email"]):
            flash("Invalid email address!")
            valid = False
        #  If password is less than 7 characters Flash message
        if len(user["password"]) < 7:
            valid = False
            flash("Password must be at least 7 characters")
        #  If password does not matcha the password confirmation Flash Message
        if not user["password"] == user["password_confirmation"]:
            flash("Password must match")
            valid = False
        
        email_already_has_account = User.get_by_email(user["email"])
        # if Email address already has an account Flash message
        if  email_already_has_account:
            flash("An account with this email already exists, please log in.")
            valid = False
            
        return valid
    
# ===================  =======================