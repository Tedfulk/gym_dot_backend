import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
    update Programs
    filter .id = <uuid>$id
    set {
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


class UpdateProgramResult(BaseModel):
    id: UUID
    name: str
    description: str | None
    active: bool | None


async def update_program(
    executor: AsyncIOExecutor,
    *,
    id: UUID,
    name: str,
    description: str,
    active: bool,
) -> UpdateProgramResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        id=id,
        name=name,
        description=description,
        active=active,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, UpdateProgramResult | None, resp, json_loads=orjson.loads
    )
    return cast(UpdateProgramResult | None, parsed)
