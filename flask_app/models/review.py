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
class Review:
    def __init__(self, review):
        self.id = review["id"]
        self.name = review["name"]
        self.stars = review["stars"]
        self.review_title = review["review_title"]
        self.message = review["message"]
        self.created_at = review["created_at"]
        self.updated_at = review["updated_at"]
        self.user = user
        self.matcha = matcha.Matcha
        
        
# =================== LEAVE REVIEW ==========================
    @classmethod
    def leave_a_review(cls, review_dict):
        if not cls.is_valid(review_dict):
            return False
        
        query = """ INSERT INTO reviews (stars, review_title, message, user_id, matcha_id)
        VALUES (%(stars)s, %(review_title)s, %(message)s, %(user_id)s, %(matcha_id)s);"""
        
        review = connectToMySQL(DB).query_db(query, review_dict)
        return review


    # =================== DELETE REVIEW ==========================

    @classmethod
    def delete_review(cls, review_id):
        
        data = {"id": review_id}
        query = """DELETE FROM reviews WHERE id = %(id)s;"""
        connectToMySQL(DB).query_db(query, data)
        
        return review_id


    # =================== UPDATE REVIEW ==========================
    @classmethod
    def update_review(cls, review_dict):
        
        review = cls.get_by_id(review_dict["id"])
        
        query = """UPDATE reviews
                SET name = %(name)s, stars = %(stars)s, review_title = %(review_title)s, message = %(message)s
                WHERE id = %(id)s;"""
        result = connectToMySQL(DB).query_db(query, review_dict)
        
        return review
    
    # ==================== GET ALL REVIEWS =====================
    
    @classmethod
    def get_all_reviews(cls):
        query = """SELECT
                reviews.id,
                reviews.created_at,
                reviews.updated_at,
                reviews.name,
                reviews.stars,
                reviews.review_title,
                reviews.message,
                users.id as user_id,
                users.first_name,
                users.last_name,
                users.email,
                users.created_at,
                users.updated_at,
                matchas.id as matcha_id,
                matchas.matcha_name,
                matchas.matcha_qty,
                matchas.matcha_short_description,
                matchas.taste_description,
                matchas.taste_notes,
                matchas.price,
                matchas.img,
                matchas.small_img_one,
                matchas.small_img_two,
                matchas.small_img_three,
                matchas.small_img_four,
                matchas.created_at,
                matchas.updated_at
                FROM reviews
                INNER JOIN matchas 
                ON matchas.id = matcha_id
                INNER JOIN users 
                ON users.id = reviews.user_id;"""
                
        review_data = connectToMySQL(DB).query_db(query)

        
        return review_data
                
                
    # =================== GET ALL REVIEWS FROM THE MATCHA SELECTED ==========================
    @classmethod
    def get_matcha_reviews(cls, matcha_name):
        data = {"matcha_name": matcha_name}
        query = """SELECT
                reviews.id,
                reviews.created_at,
                reviews.updated_at,
                reviews.name,
                reviews.stars,
                reviews.review_title,
                reviews.message,
                users.id as user_id,
                users.first_name,
                users.last_name,
                users.email,
                users.created_at,
                users.updated_at,
                matchas.id as matcha_id,
                matchas.matcha_name,
                matchas.matcha_qty,
                matchas.matcha_short_description,
                matchas.taste_description,
                matchas.taste_notes,
                matchas.price,
                matchas.img,
                matchas.small_img_one,
                matchas.small_img_two,
                matchas.small_img_three,
                matchas.small_img_four,
                matchas.created_at,
                matchas.updated_at
                FROM reviews
                INNER JOIN matchas 
                ON matchas.id = matcha_id
                INNER JOIN users 
                ON users.id = reviews.user_id
                WHERE matcha_name = %(matcha_name)s; """
        review_data = connectToMySQL(DB).query_db(query,data)
        print(f"&&&&&&&&&&&&{review_data}&&&&&&&&&&&&&")
        
        return review_data



# ============================GET MATCHA'S USER WITH REVIEWS=======
    @classmethod
    def get_matcha_user_review(cls,big_data):
        data = {"matcha_name": big_data}
        query = """ SELECT * FROM reviews
        JOIN matchas on matchas.id = reviews.matcha_id
        WHERE matcha_name = %(matcha_name)s;"""
        
        review_data = connectToMySQL(DB).query_db(query,data)
        review_matchas = []
        print(f"*****%%%%%% {data}$$$$")
        for review in review_data:
                
                print(f"####{review}")
                
                review_obj_matcha = cls(review)
                
                review_obj_matcha.matcha = matcha.Matcha(
                {
                    "id": review["id"],
                    "matcha_name": review["matcha_name"],
                    "matcha_qty": review["matcha_qty"],
                    "item_qty":review ["item_qty"],
                    "matcha_short_description": review["matcha_short_description"],
                    "taste_description": review["taste_description"],
                    "taste_notes": review["taste_notes"],
                    "price": review["price"],
                    "img": review["img"],
                    "created_at": review["created_at"],
                    "updated_at": review["updated_at"],
                    "small_img_one": review["small_img_one"],
                    "small_img_two": review["small_img_two"],
                    "small_img_three": review["small_img_three"],
                    "small_img_four": review["small_img_four"]
                    
                }
            )
                review_matchas.append(review_obj_matcha)
                print(f"^^^^^^{review_obj_matcha}")
                return review_obj_matcha

    # =================== VALIDATE REVIEW'S INPUT ==========================
    @staticmethod
    def is_valid(review_dict):
        valid = True
            
        # if len(review_dict["stars"])< 0:
        #     flash("Item rating required")
        #     valid = False
            
        if len(review_dict["review_title"]) < 3:
            flash ("Review title should be at least 3 characters")
            valid = False
            
        if len(review_dict["message"]) < 10:
            flash("Review content should be at least 10 characters")
            valid = False
        
        return valid