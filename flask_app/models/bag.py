from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app.models import matcha
from flask_app.models import bag
from flask_app.models import review
from flask_app.models import user
from flask_bcrypt import Bcrypt
import re
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.datastructures import ImmutableDict

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
        self.matcha = []
        
        
        
    @classmethod 
    def add_to_bag(cls, matcha_id_list):
        id = matcha_id_list.getlist('matcha_id')
        new_data = {'matcha_id': int(id[0])}

        query= """
        INSERT INTO
        bags (matcha_id, bags.matcha_name, matcha_qty, matcha_short_description,taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, user_id)
        
        SELECT
        id, matcha_name, matcha_qty, matcha_short_description, taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, user_id 
        FROM 
        matchas WHERE id = %(matcha_id)s;"""
        
        results = connectToMySQL(DB).query_db(query, new_data)
        
        return id


    @classmethod
    def get_bag_by_id(cls, user_id):
        data ={"id": user_id}
        query = """ SELECT bags.id matcha_name, matcha_qty, matcha_short_description,taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, users.id as user_id, first_name, last_name, email, created_at, updated_at
        FROM bags
        JOIN users on users.id = bags.user_id
        WHERE bags.id = %(id)s"""
        
        result = connectToMySQL(DB).query_db(query,data)
        print("result of query:")
        print(result)
        result = result[0]
        bags = cls(result)
    
        bag.user = user.User({
            
            "id": result["user_id"],
            "first_name": result["firs_name"],
            "last_name": result["last_name"],
            "email": result["email"],
            "created_at": result["created_at"],
            "updated_at":result["updated_at"]
            }
        )
        return bags
    
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
                    JOIN users on users.id = bags.user_id;"""
        bag_data = connectToMySQL(DB).query_db(query)
        
        bags = []
        
        for bag in bag_data:
            
            bag_obj = cls(bag)
            
            bag_obj.user = user.User(
            {
                "id": bag["user_id"],
                "first_name": bag["first_name"],
                "last_name": bag["last_name"],
                "email": bag["email"],
                "password":False,
                "created_at": bag["created_at"],
                "updated_at": bag["updated_at"]
                
            }
        )
            
            bags.append(bag_obj)
        return bags
        
        
        
        
    @classmethod
    def remove_from_bag(cls, item_id):
        
        data = {"id": item_id}
        query = """DELETE FROM bags WHERE id = %(id)s;"""
        connectToMySQL(DB).query_db(query, data)
        
        return item_id
    
    @classmethod
    def price_total(cls):
        query = """SELECT price FROM bags"""
        price = connectToMySQL(DB).query_db(query)
        total_prices = []
        for p in price:
            data = ImmutableMultiDict(p)
            total_prices.append(p["price"])
            total = sum(total_prices)
        return total
        
        