import asyncio
from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.facilities.programs import (
    AllProgramsResult,
    CreateProgramResult,
    DeleteProgramResult,
    GetLessonsResultLesson,
    GetProgramResult,
    UpdateProgramResult,
    all_programs,
    create_program,
    delete_program,
    get_lessons,
    get_program,
    update_program,
)
from gym_dot_lib.context.main import client

app = APIRouter()


@app.get("", response_model=list[AllProgramsResult])
def get_all_programs():
    programs = all_programs(executor=client)
    return asyncio.run(programs)


@app.get("/{program_id}", response_model=GetProgramResult)
def get_program_by_id(program_id: UUID):
    program = get_program(executor=client, program_id=program_id)
    return asyncio.run(program)


@app.post("", response_model=CreateProgramResult)
def make_program(name: str, description: str, active: bool):
    program = create_program(
        executor=client, name=name, description=description, active=active
    )
    return asyncio.run(program)


@app.put("/{program_id}", response_model=UpdateProgramResult)
def update_program_by_id(program_id: UUID, name: str, description: str, active: bool):
    program = update_program(
        executor=client,
        program_id=program_id,
        name=name,
        description=description,
        active=active,
    )
    return asyncio.run(program)


@app.delete("/{program_id}", response_model=DeleteProgramResult)
def delete_program_by_id(program_id: UUID):
    program = delete_program(executor=client, program_id=program_id)
    return asyncio.run(program)


@app.get("/{program_id}/lessons", response_model=list[GetLessonsResultLesson])
def get_lessons_by_program_id(program_id: UUID):
    lessons = get_lessons(executor=client, program_id=program_id)
    return asyncio.run(lessons)
