import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
    update Companies
        filter .id = <uuid>$company_id
        set {
            name := <str>$company_name,
        }
) {
    id,
    name,
}
"""


class UpdateCompanyResult(BaseModel):
    id: UUID
    name: str


async def update_company(
    executor: AsyncIOExecutor,
    *,
    company_id: UUID,
    company_name: str,
) -> UpdateCompanyResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        company_id=company_id,
        company_name=company_name,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, UpdateCompanyResult | None, resp, json_loads=orjson.loads
    )
    return cast(UpdateCompanyResult | None, parsed)
