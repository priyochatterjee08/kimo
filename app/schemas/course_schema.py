def course_serializer(course) -> dict:
    return {
        'id':str(course["_id"]),
        'name':course["name"],
        'date':course["date"],
        'description':course["description"],
        'domain':course["domain"],
        'chapters':course["chapters"],
        'rating':course["rating"]
    }

def chapter_serializer(chapter) -> list:
    return {
        'name':chapter["name"],
        'text':chapter["text"],
        'chapter_rating':chapter["chapter_rating"]
    }

def courses_serializer(courses) -> list:
    return [course_serializer(course) for course in courses]