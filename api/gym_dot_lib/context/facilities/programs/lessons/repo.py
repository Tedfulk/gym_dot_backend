import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import parse_raw_as

from .models import DeleteLessonResult, Lesson, LessonUpdates, NewLesson
from .queries import (
    ALL_LESSONS,
    CREATE_LESSON,
    DELETE_LESSON,
    GET_LESSON,
    UPDATE_LESSON,
)


class LessonRepo:
    """Methods for Lesson entity in EdgeDB."""

    @staticmethod
    async def get(
        executor: AsyncIOExecutor,
        *,
        lesson_id: UUID,
    ) -> Lesson | None:
        resp = await executor.query_single_json(
            GET_LESSON,
            lesson_id=lesson_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Lesson | None, resp, json_loads=orjson.loads
        )
        return cast(Lesson | None, parsed)

    @staticmethod
    async def create(
        executor: AsyncIOExecutor,
        *,
        new_lesson: NewLesson,
    ) -> Lesson:
        resp = await executor.query_single_json(
            CREATE_LESSON,
            class_dates=new_lesson.class_dates,
            class_times=new_lesson.class_times,
            len_of_class_time=new_lesson.len_of_class_time,
            active=new_lesson.active,
            max_attendees=new_lesson.max_attendees,
            min_attendees=new_lesson.min_attendees,
            waitlist=new_lesson.waitlist,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Lesson, resp, json_loads=orjson.loads
        )
        return cast(Lesson, parsed)

    @staticmethod
    async def update(
        executor: AsyncIOExecutor,
        *,
        lesson_id: UUID,
        updates: LessonUpdates,
    ) -> Lesson:
        resp = await executor.query_single_json(
            UPDATE_LESSON,
            lesson_id=lesson_id,
            class_dates=updates.class_dates,
            class_times=updates.class_times,
            len_of_class_time=updates.len_of_class_time,
            active=updates.active,
            max_attendees=updates.max_attendees,
            min_attendees=updates.min_attendees,
            waitlist=updates.waitlist,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Lesson, resp, json_loads=orjson.loads
        )
        return cast(Lesson, parsed)

    @staticmethod
    async def delete(
        executor: AsyncIOExecutor,
        *,
        lesson_id: UUID,
    ) -> DeleteLessonResult:
        resp = await executor.query_single_json(
            DELETE_LESSON,
            lesson_id=lesson_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, DeleteLessonResult, resp, json_loads=orjson.loads
        )
        return cast(DeleteLessonResult, parsed)

    @staticmethod
    async def all_lessons(
        executor: AsyncIOExecutor,
    ) -> list[Lesson]:
        resp = await executor.query_json(ALL_LESSONS)
        parsed = await asyncio.to_thread(
            parse_raw_as, list[Lesson], resp, json_loads=orjson.loads
        )
        return cast(list[Lesson], parsed)
