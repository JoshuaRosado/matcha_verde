from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import matcha
from flask_bcrypt import Bcrypt
import re

DB = "matcha_verde"
class Review:
    def __init__(self, review):
        self.id = review["id"]
        self.name = review["name"]
        self.stars = review["stars"]
        self.review_title = review["review_title"]
        self.message = review["message"]
        self.created_at = review["created_at"]
        self.updated_at = review["updated_at"]

@classmethod
def create_review(cls, review_dict):
    if not cls.is_valid(review_dict):
        return False
    
    query = """ INSERT INTO reviews (name, stars, review_title, message, user_id, matcha_id)
    VALUES (%(name)s, %(stars)s, %(review_title)s, %(message)s, %(user_id)s, %(matcha_id)s);"""
    
    review = connectToMySQL(DB).query_db(query, review_dict)
    return review

@classmethod
def delete_review(cls, review_id):
    
    data = {"id": review_id}
    query = """DELETE FROM reviews WHERE id = %(id)s;"""
    connectToMySQL(DB).query_db(query, data)
    
    return review_id
    
    
    
    
@staticmethod
def is_valid(matcha_dict):
    valid = True
    if len(matcha_dict["name"])< 1 :
        flash("Name should be at least 2 characters")
        valid = False
        
    if len(matcha_dict["stars"])< 0:
        flash("Choose a star rate")
        valid = False
        
    if len(matcha_dict["review_title"]) < 3:
        flash ("Review title should be at least 3 characters")
        valid = False
        
    if len(matcha_dict["message"]) < 10:
        flash("Review content should be at least 10 characters")
        valid = False
    
    return valid