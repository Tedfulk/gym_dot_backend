import asyncio
from datetime import date, time
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


@app.get("/{lesson_id}", response_model=GetLessonResult)
def get_lesson_by_id(lesson_id: UUID):
    lesson = get_lesson(executor=client, lesson_id=lesson_id)
    return asyncio.run(lesson)


@app.post("", response_model=CreateLessonResult)
def make_lesson(
    class_dates: list[date],
    class_times: list[time],
    len_of_class_time: int,
    active: bool,
    max_attendees: int,
    min_attendees: int,
    waitlist: int,
):
    lesson = create_lesson(
        executor=client,
        class_dates=class_dates,
        class_times=class_times,
        len_of_class_time=len_of_class_time,
        active=active,
        max_attendees=max_attendees,
        min_attendees=min_attendees,
        waitlist=waitlist,
    )
    return asyncio.run(lesson)


@app.put("/{lesson_id}", response_model=UpdateLessonResult)
def update_lesson_by_id(
    lesson_id: UUID,
    class_dates: list[date],
    class_times: list[time],
    len_of_class_time: int,
    active: bool,
    max_attendees: int,
    min_attendees: int,
    waitlist: int,
):
    lesson = update_lesson(
        executor=client,
        lesson_id=lesson_id,
        class_dates=class_dates,
        class_times=class_times,
        len_of_class_time=len_of_class_time,
        active=active,
        max_attendees=max_attendees,
        min_attendees=min_attendees,
        waitlist=waitlist,
    )
    return asyncio.run(lesson)


@app.delete("/{lesson_id}", response_model=DeleteLessonResult)
def delete_lesson_by_id(lesson_id: UUID):
    lesson = delete_lesson(executor=client, lesson_id=lesson_id)
    return asyncio.run(lesson)
