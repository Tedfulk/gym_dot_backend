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
async def get_all_lessons():
    return await all_lessons(executor=client)


@app.get("/{lesson_id}", response_model=GetLessonResult)
async def get_lesson_by_id(lesson_id: UUID):
    return await get_lesson(executor=client, lesson_id=lesson_id)


@app.post("", response_model=CreateLessonResult)
async def post_lesson(
    class_dates: list[date],
    class_times: list[time],
    len_of_class_time: int,
    active: bool,
    max_attendees: int,
    min_attendees: int,
    waitlist: int,
):
    return await create_lesson(
        executor=client,
        class_dates=class_dates,
        class_times=class_times,
        len_of_class_time=len_of_class_time,
        active=active,
        max_attendees=max_attendees,
        min_attendees=min_attendees,
        waitlist=waitlist,
    )


@app.put("/{lesson_id}", response_model=UpdateLessonResult)
async def put_lesson_by_id(
    lesson_id: UUID,
    class_dates: list[date],
    class_times: list[time],
    len_of_class_time: int,
    active: bool,
    max_attendees: int,
    min_attendees: int,
    waitlist: int,
):
    return await update_lesson(
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


@app.delete("/{lesson_id}", response_model=DeleteLessonResult)
async def delete_lesson_by_id(lesson_id: UUID):
    return await delete_lesson(executor=client, lesson_id=lesson_id)
