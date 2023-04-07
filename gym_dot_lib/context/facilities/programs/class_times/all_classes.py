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
"""


class AllClassesResult(BaseModel):
    id: UUID
    class_dates: list[date] | None
    class_times: list[time] | None
    len_of_class_time: int | None
    active: bool | None
    max_attendees: int | None
    min_attendees: int | None
    waitlist: int | None


async def all_classes(
    executor: AsyncIOExecutor,
) -> list[AllClassesResult]:
    resp = await executor.query_json(
        EDGEQL_QUERY,
    )
    parsed = await asyncio.to_thread(
        parse_raw_as, list[AllClassesResult], resp, json_loads=orjson.loads
    )
    return cast(list[AllClassesResult], parsed)
