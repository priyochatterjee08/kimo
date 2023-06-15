from pymongo import MongoClient
# db_connection = MongoClient("mongodb://localhost:27017")
# 2ad63b76ff12
db_connection = MongoClient("mongodb://kimo_db_1:27017")
db = db_connection.courses
collection = db["courses_info"]