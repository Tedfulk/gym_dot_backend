from uuid import UUID

from gym_dot_lib.context.facilities.programs.lessons import Lesson
from pydantic import BaseModel


class ProgramUpdates(BaseModel):
    """Fields on the Program Model that should be updatable."""

    name: str
    description: str | None
    active: bool | None


class NewProgram(ProgramUpdates):
    """Model for creating a NewProgram, extending ProgramUpdates with attributes that should be unchangable."""


class Program(NewProgram):
    """Program with 'id' field"""

    id: UUID


class ProgramWithLessons(Program):
    """Program with 'lesson' field"""

    lesson: list[Lesson]


class DeleteProgramResult(BaseModel):
    """Deleted Program with 'id' field"""

    id: UUID
