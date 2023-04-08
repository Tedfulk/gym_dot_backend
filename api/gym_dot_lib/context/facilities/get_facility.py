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
    filter .id = <uuid>$id
"""


class GetFacilityResult(BaseModel):
    id: UUID
    name: str
    address: str | None
    city: str | None
    state: str | None


async def get_facility(
    executor: AsyncIOExecutor,
    *,
    id: UUID,
) -> GetFacilityResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        id=id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, GetFacilityResult | None, resp, json_loads=orjson.loads
    )
    return cast(GetFacilityResult | None, parsed)
