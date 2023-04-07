import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
delete Lessons 
    filter .id = <uuid>$id
"""


class DeleteClassResult(BaseModel):
    id: UUID


async def delete_class(
    executor: AsyncIOExecutor,
    *,
    id: UUID,
) -> DeleteClassResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        id=id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, DeleteClassResult | None, resp, json_loads=orjson.loads
    )
    return cast(DeleteClassResult | None, parsed)
