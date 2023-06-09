import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
delete Facilities
    filter .id = <uuid>$facility_id
"""


class DeleteFacilityResult(BaseModel):
    id: UUID


async def delete_facility(
    executor: AsyncIOExecutor,
    *,
    facility_id: UUID,
) -> DeleteFacilityResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        facility_id=facility_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, DeleteFacilityResult | None, resp, json_loads=orjson.loads
    )
    return cast(DeleteFacilityResult | None, parsed)
