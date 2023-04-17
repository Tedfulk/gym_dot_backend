import pytest

from api.gym_dot_lib.context.facilities.programs.lessons import (
    CreateLessonResult,
    DeleteLessonResult,
    GetLessonResult,
    UpdateLessonResult,
    create_lesson,
    delete_lesson,
    get_lesson,
    update_lesson,
)
from api.gym_dot_lib.context.main import client
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_create_lesson():
    new_lesson = await create_lesson(
        executor=client,
        class_dates=[
            date.today(),
            date.today() + timedelta(days=1),
            date.today() + timedelta(days=2),
        ],
        class_times=[
            time(6, 0),
            time(9, 30),
            time(12, 0),
            time(16, 30),
            time(17, 30),
            time(18, 30),
        ],
        len_of_class_time=60,
        active=True,
        max_attendees=20,
        min_attendees=1,
        waitlist=10,
    )
    if new_lesson is not None:
        assert GetLessonResult(**new_lesson.dict()) == CreateLessonResult(
            **new_lesson.dict()
        )
    await delete_lesson(executor=client, lesson_id=new_lesson.id)


async def test_get_lesson(sample_lesson: CreateLessonResult):
    lesson = await get_lesson(
        executor=client,
        lesson_id=sample_lesson.id,
    )
    if lesson is not None:
        assert GetLessonResult(**lesson.dict()) == CreateLessonResult(
            **sample_lesson.dict()
        )


async def test_update_lesson(sample_lesson: CreateLessonResult):
    updated_lesson = await update_lesson(
        executor=client,
        lesson_id=sample_lesson.id,
        class_dates=[
            date.today(),
            date.today() + timedelta(days=10),
            date.today() + timedelta(days=20),
        ],
        class_times=[
            time(1, 0),
            time(2, 30),
            time(3, 0),
            time(4, 30),
            time(5, 30),
            time(6, 30),
        ],
        len_of_class_time=600,
        active=False,
        max_attendees=200,
        min_attendees=100,
        waitlist=1,
    )
    if updated_lesson is not None:
        assert GetLessonResult(**sample_lesson.dict()) != UpdateLessonResult(
            **updated_lesson.dict()
        )


async def test_delete_lesson(sample_lesson: CreateLessonResult):
    deleted_lesson = await delete_lesson(
        executor=client,
        lesson_id=sample_lesson.id,
    )
    assert deleted_lesson is not None
    lesson = await get_lesson(executor=client, lesson_id=sample_lesson.id)
    assert lesson is None
