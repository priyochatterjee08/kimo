from fastapi import APIRouter
from app.models.course_model import Courses
from app.models.course_model import Course
from app.models.course_model import Chapter
from app.schemas.course_schema import courses_serializer
from app.schemas.course_schema import course_serializer
from app.schemas.course_schema import chapter_serializer
from bson import ObjectId
from app.config.db import collection
from typing import Union

course = APIRouter()

@course.post("/")
async def create_course(course: Courses):
    _id = collection.insert_one(dict(course))
    course = courses_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": course}


@course.get("/api/v1/allcourses")
async def find_all_courses(sort: Union[int, None] = None):
   if sort == 1:
      courses = courses_serializer(collection.find().sort("name", 1))
   if sort == 2:
      courses = courses_serializer(collection.find().sort("date", -1))
   if sort == 3:
      courses = courses_serializer(collection.find().sort("rating", -1))
   else:
      courses = courses_serializer(collection.find())
   return {"status": "Ok","data": courses}
            
@course.get("/api/v1/{id}")
async def get_one_course(id: str):
   course = course_serializer(collection.find_one({"_id": ObjectId(id)}))
   return {"status": "Ok","data": course}

@course.get("/api/v1/overview/{id}")
async def get_course_overview(id: str):
   course = course_serializer(collection.find_one({"_id": ObjectId(id)}))
   return {"status": "Ok","data": course["description"]}

@course.put("/api/v1/chapter/{id}")
async def update_chapter_rating(id: str, c_rating: int, c_name: str ):
   result = collection.update_one({"_id":ObjectId(id), "chapters":{"$elemMatch":{"name": c_name}}}, {"$set": {"chapters.$.chapter_rating": c_rating}}, upsert=False)
   result_2 = collection.find_one({"_id": ObjectId(id), "rating": { "$exists": True }})
   # course = course_serializer(collection.find_one({"_id": ObjectId(id)}))
   if result_2 is not None:
      rating = result_2["rating"] + c_rating
   else:
      rating = c_rating
   result_3 = collection.update_one({"_id":ObjectId(id)}, {"$set": {"rating": rating}}, upsert= False)
   return {"status": "Ok","data": result_3.matched_count > 0 }
