from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app.models import matcha
from flask_app.models import bag
from flask_app.models import user
from flask_bcrypt import Bcrypt
import re

DB = "matcha_verde"

class Bag:
    def __init__(self, bag):
        self.id = bag["id"]
        self.matcha_name = bag["matcha_name"]
        self.matcha_qty = bag["matcha_qty"]
        self.matcha_short_description = bag["matcha_short_description"]
        self.taste_description = bag["taste_description"]
        self.taste_notes = bag["taste_notes"]
        self.price = bag["price"]
        self.img = bag["img"]
        self.created_at = bag["created_at"]
        self.updated_at = bag["updated_at"]
        self.small_img_one = bag["small_img_one"]
        self.small_img_two = bag["small_img_two"]
        self.small_img_three = bag["small_img_three"]
        self.small_img_four = bag["small_img_four"]
        self.item_qty = 0
        self.user = None
        
        
        
    @classmethod 
    def add_to_bag(cls, id):
        data = {
            'id':['id']
        }
        query = """INSERT INTO bags(matcha_name, matcha_qty, matcha_short_description,taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, users_id) SELECT matcha_name, matcha_qty, matcha_short_description, taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, user_id FROM matchas WHERE id = %(matcha_id)s ;"""
        results = connectToMySQL(DB).query_db(query,data)
        print(results)
        
        return results
    
    @classmethod
    def get_items_in_bag(cls):
        query = """SELECT * FROM bags;"""
        bag_data = connectToMySQL(DB).query_db(query)
        
        return bag_data
        
        
        
    @classmethod
    def calculate_total_price(cls, price):
        query = """SELECT price FROM bags;"""
        items_price_data = connectToMySQL(DB).query_db(query)
        
        
        
    @classmethod
    def remove_from_bag(cls, item_id):
        
        data = {"id": item_id}
        query = """DELETE FROM shopping_bags WHERE id = %(id)s;"""
        connectToMySQL(DB).query_db(query, data)
        
        return item_id
    
    @classmethod
    def price_total(cls, price):
        pass