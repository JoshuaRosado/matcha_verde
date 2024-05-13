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
    def add_to_bag(cls, id):

        query= """INSERT INTO
        bags(matcha_id,matcha_name, matcha_qty, matcha_short_description,taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, user_id)
        
        SELECT
        id, matcha_name, matcha_qty, matcha_short_description, taste_description, taste_notes, price, img, created_at, updated_at, small_img_one, small_img_two, small_img_three, small_img_four, user_id FROM 
        matchas WHERE id = %(id)s;"""
        
        # VALUES(%(bag_id)s,%(matcha_name)s, %(matcha_qty)s, %(matcha_short_description)s, %(taste_description)s, %(taste_notes)s, %(price)s, %(img)s, %(created_at)s, %(updated_at)s, %(small_img_one)s, %(small_img_two)s, %(small_img_three)s, %(small_img_four)s, %(user_id)s);"""
        
        
        #************************************ RETURNS A IMMUTABLEMULTIDICT (TUPLE INSIDE OF A LIST INSIDE OF A TUPLE)
        # NEED TO ACCESS AND RETRIEVE THE INNER DATA TO BE ABLE TO DISPLAY IT IN THE SHOPPING BAG AS THE CORRECT ITEM ADDED
        
        
        
        
        results = connectToMySQL(DB).query_db(query, id)
        print(f"************{results}")
        
        result = results
        print(result.getlist(0))
        
        
        
        
        return results

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
    def calculate_total_price(cls, price):
        query = """SELECT price FROM bags;"""
        items_price_data = connectToMySQL(DB).query_db(query)
        pass
        
        
        
    @classmethod
    def remove_from_bag(cls, item_id):
        
        data = {"id": item_id}
        query = """DELETE FROM shopping_bags WHERE id = %(id)s;"""
        connectToMySQL(DB).query_db(query, data)
        
        return item_id
    
    @classmethod
    def price_total(cls, price):
        pass