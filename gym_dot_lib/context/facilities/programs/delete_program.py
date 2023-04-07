import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
delete Programs 
    filter .id = <uuid>$id
"""


class DeleteProgramResult(BaseModel):
    id: UUID


async def delete_program(
    executor: AsyncIOExecutor,
    *,
    id: UUID,
) -> DeleteProgramResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        id=id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, DeleteProgramResult | None, resp, json_loads=orjson.loads
    )
    return cast(DeleteProgramResult | None, parsed)
