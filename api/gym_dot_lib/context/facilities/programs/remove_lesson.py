import asyncio
from datetime import date, time
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
    update Programs
        filter .id=<uuid>$program_id
        set {
            lesson -= (select detached Lessons
                filter .id=<uuid>$lesson_id )
        }
        ) {
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
"""


class RemoveLessonResultLesson(BaseModel):
    id: UUID
    class_dates: list[date] | None
    class_times: list[time] | None
    len_of_class_time: int | None
    active: bool | None
    max_attendees: int | None
    min_attendees: int | None
    waitlist: int | None


class RemoveLessonResult(BaseModel):
    id: UUID
    name: str
    description: str | None
    active: bool | None
    lesson: list[RemoveLessonResultLesson]


async def remove_lesson(
    executor: AsyncIOExecutor,
    *,
    program_id: UUID,
    lesson_id: UUID,
) -> RemoveLessonResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        program_id=program_id,
        lesson_id=lesson_id,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, RemoveLessonResult | None, resp, json_loads=orjson.loads
    )
    return cast(RemoveLessonResult | None, parsed)
