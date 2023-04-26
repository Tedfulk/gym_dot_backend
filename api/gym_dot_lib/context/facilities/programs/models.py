from uuid import UUID

from pydantic import BaseModel

from api.gym_dot_lib.context.facilities.programs.lessons import Lesson


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


class ProgramWithLessons(BaseModel):
    """Program with 'lesson' field"""

    id: UUID
    name: str
    description: str | None
    active: bool | None
    lesson: list[Lesson]


class DeleteProgramResult(BaseModel):
    """Deleted Program with 'id' field"""

    id: UUID
