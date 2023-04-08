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
}
"""


class AllProgramsResult(BaseModel):
    id: UUID
    name: str
    description: str | None
    active: bool | None


async def all_programs(
    executor: AsyncIOExecutor,
) -> list[AllProgramsResult]:
    resp = await executor.query_json(
        EDGEQL_QUERY,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, list[AllProgramsResult], resp, json_loads=orjson.loads
    )
    return cast(list[AllProgramsResult], parsed)
