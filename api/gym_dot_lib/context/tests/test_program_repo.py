import pytest

from api.gym_dot_lib.context.facilities.programs import (
    DeleteProgramResult,
    NewProgram,
    Program,
    ProgramRepo,
    ProgramUpdates,
    ProgramWithLessons,
)
from api.gym_dot_lib.context.facilities.programs.create_program_with_lesson import (
    CreateProgramWithLessonResult,
)
from api.gym_dot_lib.context.main import client
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_all_programs():
    programs = await ProgramRepo.all_programs(
        executor=client,
    )
    assert programs is not None
    assert len(programs) > 0


async def test_get_program(sample_program: Program):
    program = await ProgramRepo.get(
        executor=client,
        program_id=sample_program.id,
    )
    assert program is not None
    if program is not None:
        assert Program(**program.dict()) == Program(**sample_program.dict())


async def test_update_program(sample_program: Program):
    updated_program = await ProgramRepo.update(
        executor=client,
        program_id=sample_program.id,
        updates=ProgramUpdates(
            name=sample_program.name + " (updated)",
            description=sample_program.description + " (updated)",
            active=sample_program.active,
        ),
    )
    assert updated_program is not None
    program = await ProgramRepo.get(executor=client, program_id=updated_program.id)
    if program is not None:
        assert Program(**program.dict()) == Program(**updated_program.dict())


async def test_delete_program():
    program = await ProgramRepo.create(
        executor=client,
        new_program=NewProgram(
            name="Sample Program",
            description="Sample Program Description",
            active=True,
        ),
    )
    deleted_program = await ProgramRepo.delete(
        executor=client,
        program_id=program.id,
    )
    assert DeleteProgramResult(**deleted_program.dict()) is not None
    program = await ProgramRepo.get(executor=client, program_id=deleted_program.id)
    assert program is None


async def test_get_lessons(sample_program_with_lesson: ProgramWithLessons):
    lessons = await ProgramRepo.get_lessons(
        executor=client,
        program_id=sample_program_with_lesson.id,
    )
    if lessons is not None:
        assert lessons == ProgramWithLessons(**sample_program_with_lesson.dict())


async def test_add_and_remove_lesson_from_program(
    sample_program: Program, sample_lesson: Lesson
):
    added_lesson = await ProgramRepo.add_lesson(
        executor=client,
        program_id=sample_program.id,
        lesson_id=sample_lesson.id,
    )
    program = await ProgramRepo.get(
        executor=client,
        program_id=added_lesson.id,
    )
    if added_lesson is not None:
        removed_lesson = await ProgramRepo.remove_lesson(
            executor=client,
            program_id=program.id,
            lesson_id=added_lesson.lesson[0].id,
        )
        if removed_lesson:
            assert Program(**removed_lesson.dict()) == Program(**program.dict())
