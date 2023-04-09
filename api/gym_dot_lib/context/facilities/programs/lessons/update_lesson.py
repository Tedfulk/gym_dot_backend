import asyncio
from datetime import date, time
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
    update Lessons
    filter .id = <uuid>$lesson_id
    set {
        class_dates := <array<cal::local_date>>$class_dates,
        class_times := <array<cal::local_time>>$class_times,
        len_of_class_time := <int32>$len_of_class_time,
        active := <bool>$active,
        max_attendees := <int32>$max_attendees,
        min_attendees := <int32>$min_attendees,
        waitlist := <int32>$waitlist,
    }
) {
    id,
    class_dates,
    class_times,
    len_of_class_time,
    active,
    max_attendees,
    min_attendees,
    waitlist,
}
"""


class UpdateLessonResult(BaseModel):
    id: UUID
    class_dates: list[date] | None
    class_times: list[time] | None
    len_of_class_time: int | None
    active: bool | None
    max_attendees: int | None
    min_attendees: int | None
    waitlist: int | None


async def update_lesson(
    executor: AsyncIOExecutor,
    *,
    lesson_id: UUID,
    class_dates: list[date],
    class_times: list[time],
    len_of_class_time: int,
    active: bool,
    max_attendees: int,
    min_attendees: int,
    waitlist: int,
) -> UpdateLessonResult | None:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        lesson_id=lesson_id,
        class_dates=class_dates,
        class_times=class_times,
        len_of_class_time=len_of_class_time,
        active=active,
        max_attendees=max_attendees,
        min_attendees=min_attendees,
        waitlist=waitlist,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, UpdateLessonResult | None, resp, json_loads=orjson.loads
    )
    return cast(UpdateLessonResult | None, parsed)
