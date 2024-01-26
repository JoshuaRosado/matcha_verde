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
        # Find the user where the email matches the input email
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