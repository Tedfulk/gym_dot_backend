from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.facilities.programs import (
    AllProgramsResult,
    CreateProgramResult,
    DeleteProgramResult,
    GetLessonsResult,
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
async def get_all_programs():
    return await all_programs(executor=client)


@app.get("/{program_id}", response_model=GetProgramResult)
async def get_program_by_id(program_id: UUID):
    return await get_program(executor=client, program_id=program_id)


@app.post("", response_model=CreateProgramResult)
async def post_program(name: str, description: str, active: bool):
    return await create_program(
        executor=client, name=name, description=description, active=active
    )


@app.put("/{program_id}", response_model=UpdateProgramResult)
async def put_program_by_id(
    program_id: UUID, name: str, description: str, active: bool
):
    return await update_program(
        executor=client,
        program_id=program_id,
        name=name,
        description=description,
        active=active,
    )


@app.delete("/{program_id}", response_model=DeleteProgramResult)
async def delete_program_by_id(program_id: UUID):
    return await delete_program(executor=client, program_id=program_id)


@app.get("/{program_id}/lessons", response_model=GetLessonsResult)
async def get_lessons_by_program_id(program_id: UUID):
    return await get_lessons(executor=client, program_id=program_id)
