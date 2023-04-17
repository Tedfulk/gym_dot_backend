import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
update Programs 
    filter .id=<uuid>$program_id
    set {
        lesson -= (select detached Lessons 
            filter .id=<uuid>$lessons_id )
    }
"""


class RemoveLessonResult(BaseModel):
    id: UUID


async def remove_lesson(
    executor: AsyncIOExecutor,
    *,
    program_id: UUID,
    lessons_id: UUID,
) -> RemoveLessonResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        program_id=program_id,
        lessons_id=lessons_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, RemoveLessonResult | None, resp, json_loads=orjson.loads
    )
    return cast(RemoveLessonResult | None, parsed)
