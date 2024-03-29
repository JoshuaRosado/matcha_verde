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
        
        query = """ INSERT INTO reviews (name, stars, review_title, message, user_id, matcha_id)
        VALUES (%(name)s, %(stars)s, %(review_title)s, %(message)s, %(user_id)s, %(matcha_id)s);"""
        
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
        
    # =================== GET ALL REVIEWS ==========================
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
                INNER JOIN users 
                ON users.id = reviews.user_id
                INNER JOIN matchas 
                ON matchas.id = matcha_id; """
        review_data = connectToMySQL(DB).query_db(query)
        review_users = []
        review_matchas = []
        # for review in review_data:
            
        #     review_obj = cls(review)
            
        #     review_obj.matcha = matcha.Matcha(
        #     {
        #         "id": review["id"],
        #         "matcha_name": review["matcha_name"],
        #         "matcha_qty": review["matcha_qty"],
        #         "matcha_short_description": review["matcha_short_description"],
        #         "taste_description": review["taste_description"],
        #         "taste_notes": review["taste_notes"],
        #         "price": review["price"],
        #         "img": review["img"],
        #         "created_at": review["created_at"],
        #         "updated_at": review["updated_at"],
        #         "small_img_one": review["small_img_one"],
        #         "small_img_two": review["small_img_two"],
        #         "small_img_three": review["small_img_three"],
        #         "small_img_four": review["small_img_four"]
                
        #     }
        # )
        #     review_matchas.append(review_obj)
        
        for review in review_data:
            
            review_obj = cls(review)
            
            review_obj.user = user.User(
            {
                "id": review["id"],
                "first_name": review["first_name"],
                "last_name": review["last_name"],
                "email": review["email"],
                "password": False,
                "created_at": review["created_at"],
                "updated_at": review["updated_at"]
                
            }
        )
            review_users.append(review_obj)
        return review_users





# ============================GET MATCHA'S USER WITH REVIEWS=======
    @classmethod
    def get_matcha_user_review(cls,big_data):
        data = {"matcha_name": big_data}
        query = """ SELECT * FROM reviews
        JOIN users on users.id = reviews.user_id
        JOIN matchas on matchas.id = reviews.matcha_id
        WHERE matchas.matcha_name = %(matcha_name)s;"""
        
        results = connectToMySQL(DB).query_db(query,data)
        # NEED TO RETURN ALL REVIEWS from the each matcha_name
        for result in results:
            print(f"$$$$$$$$$$$$$$$$$$$$$$$$$${result}")
        results= result
        
        
        review = cls(results)
        
        review.user = user.User(
            {"id": results["user_id"],
                "first_name": results["first_name"],
                "last_name": results["last_name"],
                "email": results["email"],
                "password": False,
                "created_at": results["created_at"],
                "updated_at": results["updated_at"]
                }
        )
        review.matcha = matcha.Matcha(
            {
                "id": results["matcha_id"],
                "matcha_name": results["matcha_name"],
                "matcha_qty": results["matcha_qty"],
                "matcha_short_description": results ["matcha_short_description"],
                "taste_description": results["taste_description"],
                "taste_notes": results["taste_notes"],
                "price": results["price"],
                "img": results["img"],
                "small_img_one": results["small_img_one"],
                "small_img_two": results["small_img_two"],
                "small_img_three": results["small_img_three"],
                "small_img_four": results["small_img_four"],
                "created_at": results["created_at"],
                "updated_at": results["updated_at"]
                
                
            }
        )
        return review




    # =================== GET REVIEW BY ID ==========================
    @classmethod
    def get_review_by_id(cls, review_dict):
        data = {"id": review_dict}
        query = """SELECT * FROM reviews
                JOIN users on users.id = reviews.user_id
                WHERE  reviews.id = %(id)s;"""
                
        result = connectToMySQL(DB).query_db(query, data)
        review = cls(result)
        
        review.user = user.User(
            {
                "id": result["user_id"],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "email": result["email"],
                "password": False,
                "created_at": result["created_at"],
                "updated_at": result["updated_at"]
            }
        )
        return review



# ============================ GET REVIEW BY MATCHA ============

    @classmethod
    def get_reviews_by_matcha(cls, reviews_dict):
        data =  {"id" : reviews_dict}
        query  =""" SELECT * FROM reviews
        JOIN matchas on matchas.id = reviews.matcha_id
        WHERE reviews.id = %(id)s;"""
        
        result = connectToMySQL(DB).query_db(query, data)
        print("result of query:")
        print(result)
        result = result[0]
        print(result)
        review = cls(result)
        
        
        
        
        review.matcha = matcha.Matcha(
            {
                "id": result["user_id"],
                "matcha_name": result["matcha_name"],
                "matcha_qty": result["matcha_qty"],
                "matcha_short_description": result ["matcha_short_description"],
                "taste_description": result["taste_description"],
                "taste_notes": result["taste_notes"],
                "price": result["price"],
                "img": result["img"],
                "small_img_one": result["small_img_one"],
                "small_img_two": result["small_img_two"],
                "small_img_three": result["small_img_three"],
                "small_img_four": result["small_img_four"],
                "created_at": result["created_at"],
                "updated_at": result["updated_at"],
                
                
            }
        )
        return review
    # =================== VALIDATE REVIEW'S INPUT ==========================
    @staticmethod
    def is_valid(review_dict):
        valid = True
            
        if len(review_dict["stars"])< 0:
            flash("Item rating required")
            valid = False
            
        if len(review_dict["review_title"]) < 3:
            flash ("Review title should be at least 3 characters")
            valid = False
            
        if len(review_dict["message"]) < 10:
            flash("Review content should be at least 10 characters")
            valid = False
        
        return valid