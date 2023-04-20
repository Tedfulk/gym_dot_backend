import asyncio
from datetime import date, time
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import BaseModel, parse_raw_as

EDGEQL_QUERY = r"""
select (
insert Programs {
    name := <str>$name,
    description := <str>$description,
    active := <bool>$active,
    lesson := {
    (insert Lessons {
        class_dates := <array<cal::local_date>>$class_dates,
        class_times := <array<cal::local_time>>$class_times,
        len_of_class_time := <int32>$len_of_class_time,
        active := <bool>$active,
        max_attendees := <int32>$max_attendees,
        min_attendees := <int32>$min_attendees,
        waitlist := <int32>$waitlist,
    } 
    )
    }
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


class CreateProgramWithLessonResultLesson(BaseModel):
    id: UUID
    class_dates: list[date] | None
    class_times: list[time] | None
    len_of_class_time: int | None
    active: bool | None
    max_attendees: int | None
    min_attendees: int | None
    waitlist: int | None


class CreateProgramWithLessonResult(BaseModel):
    id: UUID
    name: str
    description: str | None
    active: bool | None
    lesson: list[CreateProgramWithLessonResultLesson]


async def create_program_with_lesson(
    executor: AsyncIOExecutor,
    *,
    name: str,
    description: str,
    active: bool,
    class_dates: list[date],
    class_times: list[time],
    len_of_class_time: int,
    max_attendees: int,
    min_attendees: int,
    waitlist: int,
) -> CreateProgramWithLessonResult:
    resp = await executor.query_single_json(
        EDGEQL_QUERY,
        name=name,
        description=description,
        active=active,
        class_dates=class_dates,
        class_times=class_times,
        len_of_class_time=len_of_class_time,
        max_attendees=max_attendees,
        min_attendees=min_attendees,
        waitlist=waitlist,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, CreateProgramWithLessonResult, resp, json_loads=orjson.loads
    )
    return cast(CreateProgramWithLessonResult, parsed)
