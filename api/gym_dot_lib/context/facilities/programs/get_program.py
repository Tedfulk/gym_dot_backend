import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select Programs {
    id,
    name,
    description,
    active,
} filter .id = <uuid>$program_id
"""


class GetProgramResult(BaseModel):
    id: UUID
    name: str
    description: str | None
    active: bool | None


async def get_program(
    executor: AsyncIOExecutor,
    *,
    program_id: UUID,
) -> GetProgramResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        program_id=program_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, GetProgramResult | None, resp, json_loads=orjson.loads
    )
    return cast(GetProgramResult | None, parsed)
