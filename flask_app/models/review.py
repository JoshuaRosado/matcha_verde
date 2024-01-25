from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import matcha
from flask_bcrypt import Bcrypt
import re

class Review:
    def __init__(self, review):
        self.id = review["id"]
        self.name = review["name"]
        self.stars = review["stars"]
        self.review_title = review["review_title"]
        self.message = review["message"]
        self.created_at = review["created_at"]
        self.updated_at = review["updated_at"]
        