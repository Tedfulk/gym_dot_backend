import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
    insert Programs {
        name := <str>$name,
        description := <str>$description,
        active := <bool>$active,
    }
) {
    id,
    name,
    description,
    active,
}
"""


class CreateProgramResult(BaseModel):
    id: UUID
    name: str
    description: str | None
    active: bool | None


async def create_program(
    executor: AsyncIOExecutor,
    *,
    name: str,
    description: str,
    active: bool,
) -> CreateProgramResult:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        name=name,
        description=description,
        active=active,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, CreateProgramResult, resp, json_loads=orjson.loads
    )
    return cast(CreateProgramResult, parsed)
