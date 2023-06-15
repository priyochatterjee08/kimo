from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "KIMO - new way of learning"}

from app.routes.course_routes import course
app.include_router(course)

