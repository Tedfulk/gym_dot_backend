import asyncio
from datetime import date, time
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select Lessons {
    id,
    class_dates,
    class_times,
    len_of_class_time,
    active,
    max_attendees,
    min_attendees,
    waitlist,
    }
    filter .id = <uuid>$lesson_id
"""


class GetLessonResult(BaseModel):
    id: UUID
    class_dates: list[date] | None
    class_times: list[time] | None
    len_of_class_time: int | None
    active: bool | None
    max_attendees: int | None
    min_attendees: int | None
    waitlist: int | None


async def get_lesson(
    executor: AsyncIOExecutor,
    *,
    lesson_id: UUID,
) -> GetLessonResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        lesson_id=lesson_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, GetLessonResult | None, resp, json_loads=orjson.loads
    )
    return cast(GetLessonResult | None, parsed)
