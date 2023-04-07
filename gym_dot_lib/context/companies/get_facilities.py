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
    facility: {
        id,
        address,
        city,
        name,
        state
    }
} 
filter .id=<uuid>$company_id
"""


class GetFacilitiesResultFacility(BaseModel):
    id: UUID
    address: str | None
    city: str | None
    name: str
    state: str | None


class GetFacilitiesResult(BaseModel):
    id: UUID
    name: str
    facility: list[GetFacilitiesResultFacility]


async def get_facilities(
    executor: AsyncIOExecutor,
    *,
    company_id: UUID,
) -> GetFacilitiesResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        company_id=company_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, GetFacilitiesResult | None, resp, json_loads=orjson.loads
    )
    return cast(GetFacilitiesResult | None, parsed)
