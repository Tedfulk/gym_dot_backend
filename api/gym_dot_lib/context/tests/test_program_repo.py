import pytest

from api.gym_dot_lib.context.facilities.programs import (
    AllProgramsResult,
    CreateProgramResult,
    AddLessonResult,
    RemoveLessonResult,
    DeleteProgramResult,
    GetLessonsResult,
    GetProgramResult,
    UpdateProgramResult,
    CreateProgramWithLessonResult,
    all_programs,
    create_program,
    delete_program,
    get_lessons,
    get_program,
    update_program,
    add_lesson,
    remove_lesson,
)
from api.gym_dot_lib.context.main import client
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_all_programs():
    programs = await all_programs(
        executor=client,
    )
    assert programs is not None
    assert len(programs) > 0


async def test_get_program(sample_program: CreateProgramResult):
    program = await get_program(
        executor=client,
        program_id=sample_program.id,
    )
    assert program is not None
    if program is not None:
        assert GetProgramResult(**program.dict()) == CreateProgramResult(
            **sample_program.dict()
        )


async def test_create_program():
    new_program = await create_program(
        executor=client,
        name="Sample Program 2.0",
        description="Sample Description",
        active=True,
    )
    program = await get_program(executor=client, program_id=new_program.id)
    assert new_program is not None
    if program is not None:
        assert GetProgramResult(**program.dict()) == CreateProgramResult(
            **new_program.dict()
        )
    await delete_program(executor=client, program_id=new_program.id)


async def test_update_program(sample_program: CreateProgramResult):
    updated_program = await update_program(
        executor=client,
        program_id=sample_program.id,
        name=sample_program.name + " (updated)",
        description=sample_program.description + " (updated)",
        active=sample_program.active,
    )
    assert updated_program is not None
    program = await get_program(executor=client, program_id=updated_program.id)
    if program is not None:
        assert GetProgramResult(**program.dict()) == UpdateProgramResult(
            **updated_program.dict()
        )


async def test_delete_program(sample_program: CreateProgramResult):
    deleted_program = await delete_program(
        executor=client,
        program_id=sample_program.id,
    )
    assert deleted_program is not None
    program = await get_program(executor=client, program_id=deleted_program.id)
    assert program is None


async def test_get_lessons(sample_program_with_lesson):
    lessons = await get_lessons(
        executor=client,
        program_id=sample_program_with_lesson.id,
    )
    if lessons is not None:
        assert lessons == CreateProgramWithLessonResult(
            **sample_program_with_lesson.dict()
        )
