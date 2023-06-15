from __future__ import annotations

from typing import List
from typing import Union
from pydantic import BaseModel


class Chapter(BaseModel):
    name: str
    text: str
    chapter_rating: Union[int, None] = None


class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]
    rating: Union[int, None] = None


class Courses(BaseModel):
    __root__: List[Course]
