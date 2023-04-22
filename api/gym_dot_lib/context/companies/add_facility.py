import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select(
  update Companies
    filter .id=<uuid>$company_id
    set {
      facility += (select detached Facilities
                  filter .id=<uuid>$facility_id )
    }
) {
    id,
    name,
}
"""


class AddFacilityResult(BaseModel):
    id: UUID


async def add_facility(
    executor: AsyncIOExecutor,
    *,
    company_id: UUID,
    facility_id: UUID,
) -> AddFacilityResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        company_id=company_id,
        facility_id=facility_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, AddFacilityResult | None, resp, json_loads=orjson.loads
    )
    return cast(AddFacilityResult | None, parsed)
