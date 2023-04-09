import asyncio
from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.facilities.programs.lessons import (
    AllLessonsResult,
    CreateLessonResult,
    DeleteLessonResult,
    GetLessonResult,
    UpdateLessonResult,
    all_lessons,
    create_lesson,
    delete_lesson,
    get_lesson,
    update_lesson,
)
from gym_dot_lib.context.main import client

app = APIRouter()


@app.get("", response_model=list[AllLessonsResult])
def get_all_lessons():
    lessons = all_lessons(executor=client)
    return asyncio.run(lessons)


# @app.get("/{lesson_id}", response_model=GetLessonResult)
# def get_lesson_by_id(lesson_id: UUID):
#     lesson = get_lesson(executor=client, lesson_id=lesson_id)
#     return asyncio.run(lesson)
