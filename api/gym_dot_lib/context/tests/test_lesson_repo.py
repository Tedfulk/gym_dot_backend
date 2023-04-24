import pytest

from api.gym_dot_lib.context.facilities.programs.lessons import (
    DeleteLessonResult,
    Lesson,
    LessonRepo,
    LessonUpdates,
    NewLesson,
)
from api.gym_dot_lib.context.main import client
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_get_lesson(sample_lesson: Lesson):
    lesson = await LessonRepo.get(
        executor=client,
        lesson_id=sample_lesson.id,
    )
    if lesson is not None:
        assert Lesson(**lesson.dict()) == Lesson(**sample_lesson.dict())


async def test_update_lesson(sample_lesson: Lesson):
    updated_lesson = await LessonRepo.update(
        executor=client,
        lesson_id=sample_lesson.id,
        updates=LessonUpdates(
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
        ),
    )
    if updated_lesson is not None:
        assert Lesson(**sample_lesson.dict()) != Lesson(**updated_lesson.dict())


async def test_delete_lesson():
    sample_lesson = await LessonRepo.create(
        executor=client,
        new_lesson=NewLesson(
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
            max_attendees=20,
            min_attendees=1,
            waitlist=10,
        ),
    )
    deleted_lesson = await LessonRepo.delete(
        executor=client,
        lesson_id=sample_lesson.id,
    )
    assert DeleteLessonResult(**deleted_lesson.dict()) is not None
    lesson = await LessonRepo.get(executor=client, lesson_id=sample_lesson.id)
    assert lesson is None
