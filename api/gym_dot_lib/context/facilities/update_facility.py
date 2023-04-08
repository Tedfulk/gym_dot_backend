import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
    update Facilities
    filter .id = <uuid>$id
    set {
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
    state,
}
"""


class UpdateFacilityResult(BaseModel):
    id: UUID
    name: str
    address: str | None
    city: str | None
    state: str | None


async def update_facility(
    executor: AsyncIOExecutor,
    *,
    id: UUID,
    name: str,
    address: str,
    city: str,
    state: str,
) -> UpdateFacilityResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        id=id,
        name=name,
        address=address,
        city=city,
        state=state,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, UpdateFacilityResult | None, resp, json_loads=orjson.loads
    )
    return cast(UpdateFacilityResult | None, parsed)
