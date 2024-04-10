from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import review
from flask_app.models import matcha
from flask_app.models import user
from flask_bcrypt import Bcrypt
import re

DB = "matcha_verde"

class Shopping_bag:
    def __init__(self, shopping_bag):
        self.id = shopping_bag['id']
    