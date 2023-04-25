import pytest

from api.gym_dot_lib.context.facilities.programs import (
    DeleteProgramResult,
    NewProgram,
    Program,
    ProgramUpdates,
    ProgramWithLessons,
)
from api.gym_dot_lib.context.facilities.programs.lessons import Lesson
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_get_all_programs():
    """GET /programs"""
    response = await AC.get("/programs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


async def test_get_program_by_id(sample_program: Program):
    """GET /programs/{program_id}"""
    response = await AC.get(f"/programs/{sample_program.id}")
    assert response.status_code == 200
    assert Program(**response.json()) == sample_program.dict()


async def test_post_program():
    """POST /programs"""
    new_program = NewProgram(name="Test Program")
    resp = await AC.post("/programs", data=new_program.json())
    program_id = resp.json()["id"]
    program = await AC.get(f"/programs/{program_id}")
    assert resp.status_code == 200
    assert resp.json() == program.json()
    await AC.delete(f"/programs/{program_id}")


async def test_put_program_by_id(sample_program: Program):
    """PUT /programs/{program_id}"""
    updates = ProgramUpdates(
        **{**sample_program.dict(), "name": sample_program.name + "(Updated)"}
    )
    updated_program = await AC.put(
        f"/programs/{sample_program.id}",
        data=updates.json(),
    )
    updated_program_id = updated_program.json()["id"]
    program = await AC.get(f"/programs/{updated_program_id}")
    assert updated_program.status_code == 200
    assert updated_program.json() == program.json()


async def test_delete_program_by_id():
    """DELETE /programs/{program_id}"""
    new_program = NewProgram(name="Test Program")
    resp = await AC.post("/programs", data=new_program.json())
    program_id = resp.json()["id"]
    resp = await AC.delete(f"/programs/{program_id}")
    assert resp.status_code == 200
    assert DeleteProgramResult(**resp.json())


async def test_get_all_lessons(sample_program_with_lesson: ProgramWithLessons):
    """GET /programs/{program_id}/lessons"""
    response = await AC.get(f"/programs/{sample_program_with_lesson.id}/lessons")
    assert response.status_code == 200
    assert ProgramWithLessons(**response.json()) == sample_program_with_lesson.dict()
