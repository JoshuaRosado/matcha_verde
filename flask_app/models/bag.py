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
        self.user = None
        
        
        
    @classmethod 
    def add_to_bag(cls, item_id):
        
        query = """INSERT INTO bags SELECT * FROM matchas WHERE id = %(id)s;"""
        connectToMySQL(DB).query_db(query)
        
        return item_id
    
    @classmethod
    def get_items_in_bag(cls):
        # query = """ SELECT 
        #             bags.id, bags.created_at, bags.updated_at,matcha_name, matcha_qty, matcha_short_description, taste_description, taste_notes, price, img, small_img_one,small_img_two, small_img_three, small_img_four, users.id as user_id,first_name,last_name,email, users.created_at, users.updated_at
        #             FROM bags
        #             JOIN users on users.id = bags.user_id;"""
        
        query = """SELECT * FROM bags;"""
        bag_data = connectToMySQL(DB).query_db(query)
        bag_data = bag_data[0]
        bag = cls(bag_data)
        
        return bag
        
        # bags = []
        
        # for bag in bag_data:
        #     print(bag)
            
        #     bag_obj = cls(bag)
            
        #     bag_obj.user = user.User(
        #         {
        #             "id": bag["user_item_id"],
        #             "first_name": bag["first_name"],
        #             "last_name": bag["last_name"],
        #             "email": bag["email"],
        #             "password":False,
        #             "created_at": bag["created_at"],
        #             "updated_at": bag["updated_at"]
                    
        #         }
        #     )
            
        #     bags.append(bag_obj)
        # return bags
        
        
    @classmethod
    def remove_from_bag(cls, item_id):
        
        data = {"id": item_id}
        query = """DELETE FROM shopping_bags WHERE id = %(id)s;"""
        connectToMySQL(DB).query_db(query, data)
        
        return item_id
    
    