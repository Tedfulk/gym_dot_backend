import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select Facilities {
    id,
    name,
    address,
    city,
    state,
}
"""


class AllFacilitiesResult(BaseModel):
    id: UUID
    name: str
    address: str | None
    city: str | None
    state: str | None


async def all_facilities(
    executor: AsyncIOExecutor,
) -> list[AllFacilitiesResult]:
    resp = await executor.query_json(
        EDGEQL_QUERY,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, list[AllFacilitiesResult], resp, json_loads=orjson.loads
    )
    return cast(list[AllFacilitiesResult], parsed)
