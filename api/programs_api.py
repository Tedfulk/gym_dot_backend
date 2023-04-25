from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.facilities.programs import (
    DeleteProgramResult,
    NewProgram,
    Program,
    ProgramRepo,
    ProgramUpdates,
    ProgramWithLessons,
)
from gym_dot_lib.context.main import client

app = APIRouter()


@app.get("", response_model=list[Program])
async def get_all_programs():
    return await ProgramRepo.all_programs(executor=client)


@app.get("/{program_id}", response_model=Program)
async def get_program_by_id(program_id: UUID):
    return await ProgramRepo.get(executor=client, program_id=program_id)


@app.post("", response_model=Program)
async def post_program(new_program: NewProgram):
    return await ProgramRepo.create(
        executor=client,
        new_program=NewProgram(
            name=new_program.name,
            description=new_program.description,
            active=new_program.active,
        ),
    )


@app.put("/{program_id}", response_model=Program)
async def put_program_by_id(
    program_id: UUID,
    updates: ProgramUpdates,
):
    return await ProgramRepo.update(
        executor=client,
        program_id=program_id,
        updates=ProgramUpdates(
            name=updates.name,
            description=updates.description,
            active=updates.active,
        ),
    )


@app.delete("/{program_id}", response_model=DeleteProgramResult)
async def delete_program_by_id(program_id: UUID):
    return await ProgramRepo.delete(executor=client, program_id=program_id)


@app.get("/{program_id}/lessons", response_model=ProgramWithLessons)
async def get_lessons_by_program_id(program_id: UUID):
    return await ProgramRepo.get_lessons(executor=client, program_id=program_id)
