import pytest

from api.gym_dot_lib.context.facilities.programs.lessons import (
    DeleteLessonResult,
    Lesson,
    LessonRepo,
    LessonUpdates,
    NewLesson,
)
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_get_all_lessons():
    """GET /lessons"""
    response = await AC.get("/lessons")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


async def test_get_lesson_by_id(sample_lesson: Lesson):
    """GET /lessons/{lesson_id}"""
    response = await AC.get(f"/lessons/{sample_lesson.id}")
    assert response.status_code == 200
    assert Lesson(**response.json()) == sample_lesson.dict()


async def test_post_lesson():
    """POST /lessons"""
    new_lesson = NewLesson(
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
    resp = await AC.post("/lessons", data=new_lesson.json())
    lesson_id = resp.json()["id"]
    lesson = await AC.get(f"/lessons/{lesson_id}")
    assert resp.status_code == 200
    assert resp.json() == lesson.json()
    await AC.delete(f"/lessons/{lesson_id}")


async def test_put_lesson_by_id(sample_lesson: Lesson):
    """PUT /lessons/{lesson_id}"""
    updates = LessonUpdates(
        **{**sample_lesson.dict(), "max_attendees": sample_lesson.max_attendees + 1}
    )
    updated_lesson = await AC.put(
        f"/lessons/{sample_lesson.id}",
        data=updates.json(),
    )
    updated_lesson_id = updated_lesson.json()["id"]
    lesson = await AC.get(f"/lessons/{updated_lesson_id}")
    assert updated_lesson.status_code == 200
    assert updated_lesson.json() == lesson.json()


async def test_delete_lesson_by_id():
    """DELETE /lessons/{lesson_id}"""
    new_lesson = NewLesson(
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
    resp = await AC.post("/lessons", data=new_lesson.json())
    lesson_id = resp.json()["id"]
    delete_resp = await AC.delete(f"/lessons/{lesson_id}")
    assert delete_resp.status_code == 200
    assert (
        DeleteLessonResult(**delete_resp.json())
        == DeleteLessonResult(id=lesson_id).dict()
    )
