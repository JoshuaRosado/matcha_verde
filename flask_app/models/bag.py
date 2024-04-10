from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import matcha
from flask_app.models import bag
from flask_app.models import user
from flask_bcrypt import Bcrypt
import re

DB = "matcha_verde"

class Bag:
    def __init__(self, shopping_bag):
        self.id = shopping_bag['id']
        self.user = None
        self.matcha = matcha
        
        
        
    @classmethod 
    def add_to_bag(cls, item_id):
        
        query = """INSERT INTO bags SELECT * FROM matchas WHERE id = %(id)s;"""
        connectToMySQL(DB).query_db(query)
        
        return item_id
    
    
    @classmethod
    def remove_from_bag(cls, item_id):
        
        data = {"id": item_id}
        query = """DELETE FROM shopping_bags WHERE id = %(id)s;"""
        connectToMySQL(DB).query_db(query, data)
        
        return item_id
    
    