import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
    insert Facilities {
        name := <str>$name,
        address := <str>$address,
        city := <str>$city,
        state := <str>$state,
    }
) {
    id,
    name,
    address,
    city,
    state
}
"""


class CreateFacilityResult(BaseModel):
    id: UUID
    name: str
    address: str | None
    city: str | None
    state: str | None


async def create_facility(
    executor: AsyncIOExecutor,
    *,
    name: str,
    address: str,
    city: str,
    state: str,
) -> CreateFacilityResult:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        name=name,
        address=address,
        city=city,
        state=state,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, CreateFacilityResult, resp, json_loads=orjson.loads
    )
    return cast(CreateFacilityResult, parsed)
