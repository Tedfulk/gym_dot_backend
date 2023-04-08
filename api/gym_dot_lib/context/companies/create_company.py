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
    }
) {
    id,
    name
}
"""


class CreateCompanyResult(BaseModel):
    id: UUID
    name: str


async def create_company(
    executor: AsyncIOExecutor,
    *,
    company_name: str,
) -> CreateCompanyResult:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        company_name=company_name,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, CreateCompanyResult, resp, json_loads=orjson.loads
    )
    return cast(CreateCompanyResult, parsed)
