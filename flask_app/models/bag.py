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
    def __init__(self, matcha_bag):
        self.id = matcha_bag["id"]
        self.matcha_name = matcha_bag["matcha_name"]
        self.matcha_qty = matcha_bag["matcha_qty"]
        self.matcha_short_description = matcha_bag["matcha_short_description"]
        self.taste_description = matcha_bag["taste_description"]
        self.taste_notes = matcha_bag["taste_notes"]
        self.price = matcha_bag["price"]
        self.img = matcha_bag["img"]
        self.created_at = matcha_bag["created_at"]
        self.updated_at = matcha_bag["updated_at"]
        self.small_img_one = matcha_bag["small_img_one"]
        self.small_img_two = matcha_bag["small_img_two"]
        self.small_img_three = matcha_bag["small_img_three"]
        self.small_img_four = matcha_bag["small_img_four"]
        self.item_qty = 0
        self.user = None
        
        
        
    @classmethod 
    def add_to_bag(cls, matcha_id):

        query = """INSERT INTO bags(matcha_name, matcha_qty, matcha_short_description,taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, user_bag_id) SELECT matcha_name, matcha_qty, matcha_short_description, taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, user_id FROM matchas WHERE id = %(bag_id)s ;"""
        results = connectToMySQL(DB).query_db(query,matcha_id)
        print(f"****************************************{results}")
        
        return results
    
    @classmethod
    def get_items_in_bag(cls):
        query = """SELECT * FROM bags;"""
        bag_data = connectToMySQL(DB).query_db(query)
        
        return bag_data
        
    @classmethod
    def get_all_matchas_in_bag(cls):
        query = """ SELECT 
                    bags.id, bags.created_at, bags.updated_at,matcha_name, matcha_qty, matcha_short_description, taste_description, taste_notes, price, img, small_img_one,small_img_two, small_img_three, small_img_four, users.id as user_id,first_name,last_name,email, users.created_at, users.updated_at
                    FROM bags
                    JOIN users on users.id = bags.user_bag_id;"""
        bag_data = connectToMySQL(DB).query_db(query)
        
        bags = []
        
        for matcha_bag in bag_data:
            
            bag_obj = cls(bag)
            
            bag_obj.user = user.User(
                {
                    "id": matcha_bag["user_id"],
                    "first_name": matcha_bag["first_name"],
                    "last_name": matcha_bag["last_name"],
                    "email": matcha_bag["email"],
                    "password":False,
                    "created_at": matcha_bag["created_at"],
                    "updated_at": matcha_bag["updated_at"]
                    
                }
            )
            
            bags.append(bag_obj)
        return bags
        
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