import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
delete Lessons
    filter .id = <uuid>$lesson_id
"""


class DeleteLessonResult(BaseModel):
    id: UUID


async def delete_lesson(
    executor: AsyncIOExecutor,
    *,
    lesson_id: UUID,
) -> DeleteLessonResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        lesson_id=lesson_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, DeleteLessonResult | None, resp, json_loads=orjson.loads
    )
    return cast(DeleteLessonResult | None, parsed)
