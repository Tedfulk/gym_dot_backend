import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
insert Companies {
    name := <str>$company_name,
    facility := {
    (insert Facilities {
        name := <str>$facility_name,
        address := <str>$address,
        city := <str>$city,
        state := <str>$state,
    }
    )
    }
}
) {
    id,
    name,
    facility: {
    id,
    name,
    address,
    city,
    state
    }
}
"""


class CreateCompanyAndFacilityResultFacility(BaseModel):
    id: UUID
    name: str
    address: str | None
    city: str | None
    state: str | None


class CreateCompanyAndFacilityResult(BaseModel):
    id: UUID
    name: str
    facility: list[CreateCompanyAndFacilityResultFacility]


async def create_company_and_facility(
    executor: AsyncIOExecutor,
    *,
    company_name: str,
    facility_name: str,
    address: str,
    city: str,
    state: str,
) -> CreateCompanyAndFacilityResult:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        company_name=company_name,
        facility_name=facility_name,
        address=address,
        city=city,
        state=state,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, CreateCompanyAndFacilityResult, resp, json_loads=orjson.loads
    )
    return cast(CreateCompanyAndFacilityResult, parsed)
