from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import matcha
import re

class User :
    def __init__(self, user):
        self.id = user["id"]
        self.first_name = user["first_name"]
        self.last_name = user["last_name"]
        self.email = user["email"]
        self.password = user["password"]
        self.created_at = user["created_at"]
        self.updated_at = user["updated_at"]
        self.matcha = []