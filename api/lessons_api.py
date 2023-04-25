from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.main import client

from api.gym_dot_lib.context.facilities.programs.lessons import (
    DeleteLessonResult,
    Lesson,
    LessonRepo,
    LessonUpdates,
    NewLesson,
)

app = APIRouter()


@app.get("", response_model=list[Lesson])
async def get_all_lessons():
    return await LessonRepo.all_lessons(executor=client)


@app.get("/{lesson_id}", response_model=Lesson)
async def get_lesson_by_id(lesson_id: UUID):
    return await LessonRepo.get(executor=client, lesson_id=lesson_id)


@app.post("", response_model=Lesson)
async def post_lesson(
    new_lesson: NewLesson,
):
    return await LessonRepo.create(
        executor=client,
        new_lesson=NewLesson(
            class_dates=new_lesson.class_dates,
            class_times=new_lesson.class_times,
            len_of_class_time=new_lesson.len_of_class_time,
            active=new_lesson.active,
            max_attendees=new_lesson.max_attendees,
            min_attendees=new_lesson.min_attendees,
            waitlist=new_lesson.waitlist,
        ),
    )


@app.put("/{lesson_id}", response_model=Lesson)
async def put_lesson_by_id(
    lesson_id: UUID,
    updates: LessonUpdates,
):
    return await LessonRepo.update(
        executor=client,
        lesson_id=lesson_id,
        updates=LessonUpdates(
            class_dates=updates.class_dates,
            class_times=updates.class_times,
            len_of_class_time=updates.len_of_class_time,
            active=updates.active,
            max_attendees=updates.max_attendees,
            min_attendees=updates.min_attendees,
            waitlist=updates.waitlist,
        ),
    )


@app.delete("/{lesson_id}", response_model=DeleteLessonResult)
async def delete_lesson_by_id(lesson_id: UUID):
    return await LessonRepo.delete(executor=client, lesson_id=lesson_id)
