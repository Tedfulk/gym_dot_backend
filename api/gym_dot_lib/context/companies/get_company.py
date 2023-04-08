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
    filter .id = <uuid>$company_id
"""


class GetCompanyResult(BaseModel):
    id: UUID
    name: str


async def get_company(
    executor: AsyncIOExecutor,
    *,
    company_id: UUID,
) -> GetCompanyResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        company_id=company_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, GetCompanyResult | None, resp, json_loads=orjson.loads
    )
    return cast(GetCompanyResult | None, parsed)
