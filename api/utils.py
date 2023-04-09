import itertools as iter
from typing import Optional, Type

from pydantic import BaseModel

from gym_dot_lib.context.utils.str_enum import StrEnum


class Tag(StrEnum):
    """Enum to tag groups of api endpoints. Used to create the sections of the interative openapi docs."""

    companies = "Companies"
    facilities = "Facilities"
    programs = "Programs"
    lessons = "Lessons"


def servers():
    return [
        {
            "url": "http://localhost:8000",
            "description": "Local server",
        },
    ]


def description(*tags: Type[StrEnum]):
    """Helper function to make an openapi description string for the subrouters.

    Note: the tag values can't have any spaces since they are used to make
          html element ids.

    Adds heading links to tagged groups of endpoints in the api docs, so a user
    of the interactive docs can click to jump to the relevant api section.

    Args:
        tags: Any number of utils.StrEnum objects
    """
    tag_values = (tag.value for tag in iter.chain(*tags))
    return "".join(
        [
            f'+ <a href="#operations-tag-{tag}"><b>{tag} API</b></a>\n\n'
            for tag in tag_values
        ]
    )


class ErrorDetail(BaseModel):
    msg: str
    loc: Optional[list[str]] = None


class ErrorModel(BaseModel):
    """Used to type-annotate the custom error responses, mostly for the openapi docs."""

    detail: list[ErrorDetail]


def error(*, msg: str, loc: Optional[list[str]] = None):
    """Helper function used to format a custom exception's response body into a format that matches the default FastAPI behavior.

    Example:
        except TransactionCanceledException:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=error(msg="Detailed message relaying what caused the exception."),
            )
    """

    return [ErrorDetail(msg=msg, loc=loc).dict()]
