from datetime import date, time
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class LessonUpdates(BaseModel):
    """Fields on the Lesson Model that should be updatable."""

    class_dates: list[date] | None
    class_times: list[time] | None
    len_of_class_time: int | None
    active: bool | None
    max_attendees: int | None
    min_attendees: int | None
    waitlist: int | None


class NewLesson(LessonUpdates):
    """Model for creating a NewLesson, extending LessonUpdates with attributes that should be unchangable. Has a 'program_id' field."""


class Lesson(NewLesson):
    """Lesson with 'id' field"""

    id: UUID


class DeleteLessonResult(BaseModel):
    """Deleted Lesson with 'id' field"""

    id: UUID
