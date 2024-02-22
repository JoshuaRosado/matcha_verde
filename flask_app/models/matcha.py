from flask_app import app
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user


DB = "matcha_verde"

class Matcha:
    def __init__(self, matcha):
        self.id = matcha["id"]
        self.matcha_name = matcha["matcha_name"]
        self.matcha_qty = matcha["matcha_qty"]
        self.matcha_short_description = matcha["matcha_short_description"]
        self.taste_description = matcha["taste_description"]
        self.matcha_specification = matcha["matcha_specification"]
        self.taste_notes = matcha["taste_notes"]
        self.price = matcha["price"]
        self.img = matcha["img"]
        self.created_at = matcha["created_at"]
        self.updated_at = matcha["updated_at"]

    @classmethod
    def get_by_id(cls, matcha_dict):
        
        data = {"id": matcha_dict}
        query = """ SELECT * FROM matchas JOIN users on users.id = matchas.user_id WHERE matchas.id = %(id)s"""
        
        results = connectToMySQL(DB).query_db(query,data)
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
    def get_all(cls):
        query = """ SELECT 
                    matchas.id, matchas.created_at, matchas.updated_at, matchas.matcha_name, matchas.matcha_qty, matchas.matcha_short_description, matchas.taste_description, matchas.matcha_specification, matchas.taste_notes, matchas.price, matchas.img, users.id as user_id, users.first_name, users.last_name, users.email, users.created_at, users.updated_at
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
            
        
            