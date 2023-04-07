import asyncio
from datetime import date, time
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select Programs {
    id,
    name,
    description,
    active,
    lesson: {
        id,
        class_dates,
        class_times,
        len_of_class_time,
        active,
        max_attendees,
        min_attendees,
        waitlist,
    }
} 
filter .id=<uuid>$program_id
"""


class GetClassesResultLesson(BaseModel):
    id: UUID
    class_dates: list[date] | None
    class_times: list[time] | None
    len_of_class_time: int | None
    active: bool | None
    max_attendees: int | None
    min_attendees: int | None
    waitlist: int | None


class GetClassesResult(BaseModel):
    id: UUID
    name: str
    description: str | None
    active: bool | None
    lesson: list[GetClassesResultLesson]


async def get_classes(
    executor: AsyncIOExecutor,
    *,
    program_id: UUID,
) -> GetClassesResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        program_id=program_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, GetClassesResult | None, resp, json_loads=orjson.loads
    )
    return cast(GetClassesResult | None, parsed)
