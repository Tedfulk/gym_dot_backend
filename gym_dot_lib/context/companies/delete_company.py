import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
delete Companies
    filter .id = <uuid>$company_id
"""


class DeleteCompanyResult(BaseModel):
    id: UUID


async def delete_company(
    executor: AsyncIOExecutor,
    *,
    company_id: UUID,
) -> DeleteCompanyResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        company_id=company_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, DeleteCompanyResult | None, resp, json_loads=orjson.loads
    )
    return cast(DeleteCompanyResult | None, parsed)
