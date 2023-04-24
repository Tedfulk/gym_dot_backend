import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import parse_raw_as

from api.gym_dot_lib.context.facilities.programs.lessons import NewLesson

from .models import (
    DeleteProgramResult,
    NewProgram,
    Program,
    ProgramUpdates,
    ProgramWithLessons,
)
from .queries import (
    ADD_LESSON,
    ALL_PROGRAMS,
    CREATE_PROGRAM,
    CREATE_PROGRAM_WITH_LESSON,
    DELETE_PROGRAM,
    GET_LESSONS,
    GET_PROGRAM,
    REMOVE_LESSON,
    UPDATE_PROGRAM,
)


class ProgramRepo:
    """Methods for Program entity in EdgeDB."""

    @staticmethod
    async def get(
        executor: AsyncIOExecutor,
        *,
        program_id: UUID,
    ) -> Program | None:
        resp = await executor.query_single_json(
            GET_PROGRAM,
            program_id=program_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Program | None, resp, json_loads=orjson.loads
        )
        return cast(Program | None, parsed)

    @staticmethod
    async def create(
        executor: AsyncIOExecutor,
        *,
        new_program: NewProgram,
    ) -> Program:
        resp = await executor.query_single_json(
            CREATE_PROGRAM,
            name=new_program.name,
            description=new_program.description,
            active=new_program.active,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Program, resp, json_loads=orjson.loads
        )
        return cast(Program, parsed)

    @staticmethod
    async def update(
        executor: AsyncIOExecutor,
        *,
        program_id: UUID,
        updates: ProgramUpdates,
    ) -> Program:
        resp = await executor.query_single_json(
            UPDATE_PROGRAM,
            program_id=program_id,
            name=updates.name,
            description=updates.description,
            active=updates.active,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Program, resp, json_loads=orjson.loads
        )
        return cast(Program, parsed)

    @staticmethod
    async def delete(
        executor: AsyncIOExecutor,
        *,
        program_id: UUID,
    ) -> DeleteProgramResult:
        resp = await executor.query_single_json(
            DELETE_PROGRAM,
            program_id=program_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, DeleteProgramResult, resp, json_loads=orjson.loads
        )
        return cast(DeleteProgramResult, parsed)

    @staticmethod
    async def all_programs(
        executor: AsyncIOExecutor,
    ) -> list[Program]:
        resp = await executor.query_json(
            ALL_PROGRAMS,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, list[Program], resp, json_loads=orjson.loads
        )
        return cast(list[Program], parsed)

    @staticmethod
    async def add_lesson(
        executor: AsyncIOExecutor,
        *,
        program_id: UUID,
        lesson_id: UUID,
    ) -> ProgramWithLessons:
        resp = await executor.query_single_json(
            ADD_LESSON,
            program_id=program_id,
            lesson_id=lesson_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, ProgramWithLessons, resp, json_loads=orjson.loads
        )
        return cast(ProgramWithLessons, parsed)

    @staticmethod
    async def remove_lesson(
        executor: AsyncIOExecutor,
        *,
        program_id: UUID,
        lesson_id: UUID,
    ) -> Program:
        resp = await executor.query_single_json(
            REMOVE_LESSON,
            program_id=program_id,
            lesson_id=lesson_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Program, resp, json_loads=orjson.loads
        )
        return cast(Program, parsed)

    @staticmethod
    async def get_lessons(
        executor: AsyncIOExecutor,
        *,
        program_id: UUID,
    ) -> ProgramWithLessons | None:
        resp = await executor.query_single_json(
            GET_LESSONS,
            program_id=program_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, ProgramWithLessons | None, resp, json_loads=orjson.loads
        )
        return cast(ProgramWithLessons | None, parsed)

    @staticmethod
    async def create_program_with_lesson(
        executor: AsyncIOExecutor,
        *,
        new_program: NewProgram,
        new_lesson: NewLesson,
    ) -> ProgramWithLessons:
        resp = await executor.query_single_json(
            CREATE_PROGRAM_WITH_LESSON,
            name=new_program.name,
            description=new_program.description,
            active=new_program.active,
            class_dates=new_lesson.class_dates,
            class_times=new_lesson.class_times,
            len_of_class_time=new_lesson.len_of_class_time,
            max_attendees=new_lesson.max_attendees,
            min_attendees=new_lesson.min_attendees,
            waitlist=new_lesson.waitlist,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, ProgramWithLessons, resp, json_loads=orjson.loads
        )
        return cast(ProgramWithLessons, parsed)
