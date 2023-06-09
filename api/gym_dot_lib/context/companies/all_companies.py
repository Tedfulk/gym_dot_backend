import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select Companies {
        id,
        name,
}
"""


class AllCompaniesResult(BaseModel):
    id: UUID
    name: str


async def all_companies(
    executor: AsyncIOExecutor,
) -> list[AllCompaniesResult]:
    resp = await executor.query_json(
        EDGEQL_QUERY,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, list[AllCompaniesResult], resp, json_loads=orjson.loads
    )
    return cast(list[AllCompaniesResult], parsed)
