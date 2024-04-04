from flask_app import app
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
from flask_app.models import review


DB = "matcha_verde"

class Matcha:
    def __init__(self, matcha):
        self.id = matcha["id"]
        self.matcha_name = matcha["matcha_name"]
        self.matcha_qty = matcha["matcha_qty"]
        self.matcha_short_description = matcha["matcha_short_description"]
        self.taste_description = matcha["taste_description"]
        self.taste_notes = matcha["taste_notes"]
        self.price = matcha["price"]
        self.img = matcha["img"]
        self.created_at = matcha["created_at"]
        self.updated_at = matcha["updated_at"]
        self.small_img_one = matcha["small_img_one"]
        self.small_img_two = matcha["small_img_two"]
        self.small_img_three = matcha["small_img_three"]
        self.small_img_four = matcha["small_img_four"]
        self.reviews = review
        self.user = None



    @classmethod
    def get_matcha_name(cls, matcha_dict):
        data = {"matcha_name": matcha_dict}
        query = """ SELECT * FROM matchas JOIN users on users.id = matchas.user_id WHERE matchas.matcha_name = %(matcha_name)s;"""
        
        results = connectToMySQL(DB).query_db(query,data)
        results = results[0]
        matcha = cls(results)
        
        matcha.user = user.User(
            {
                "id": results["user_id"],
                "first_name":results["first_name"],
                "last_name": results["last_name"],
                "email": results["email"],
                "password": results["password"],
                "created_at": results["created_at"],
                "updated_at": results["updated_at"],
            }
        )
        return matcha
    
    @classmethod
    def get_all_matchas(cls):
        query = """ SELECT 
                    matchas.id, matchas.created_at, matchas.updated_at,matcha_name, matcha_qty, matcha_short_description, taste_description, taste_notes, price, img, small_img_one,small_img_two, small_img_three, small_img_four, users.id as user_id,first_name,last_name,email, users.created_at, users.updated_at
                    FROM matchas
                    JOIN users on users.id = matchas.user_id;"""
        matcha_data = connectToMySQL(DB).query_db(query)
        
        matchas = []
        
        for matcha in matcha_data:
            
            matcha_obj = cls(matcha)
            
            matcha_obj.user = user.User(
                {
                    "id": matcha["user_id"],
                    "first_name": matcha["first_name"],
                    "last_name": matcha["last_name"],
                    "email": matcha["email"],
                    "password":False,
                    "created_at": matcha["created_at"],
                    "updated_at": matcha["updated_at"]
                    
                }
            )
            
            matchas.append(matcha_obj)
        return matchas
    
    
    # ==================== USER QUIZ FUNCTION (retrieving) ==============
    @classmethod
    def start_quiz():
        print("Get to know your type of matcha")
        q1 = input("Matcha type, regular or organic?")
        options_q1 = ["regular", "organic"]
        if q1 == options_q1[0]:
            q1_regular = input("Do you prefer strong rich flavor or light smooth?")
            options_q1_regular = ["strong rich","light smooth"]
            if q1_regular == options_q1_regular[0]:
                print("Sayaka and Ummon")
            elif q1_regular == options_q1_regular[1]:
                print("Hatsu")
            else:
                False
                
        elif q1 == options_q1[1]:
            q1_organic = input("Do you prefer a light and snappy flavor or more robust?")
            options_q1_organic = ["light and snappy", "robust"]
            if q1_organic == options_q1_organic[0]:
                print("Organic Matcha")
            elif q1_organic == options_q1_organic[1]:
                print("Premium Organic Matcha")
            else: 
                False
        else:
            False
        
        
        