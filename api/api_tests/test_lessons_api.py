import pytest

from api.gym_dot_lib.context.facilities.programs.lessons import (
    all_lessons,
    AllLessonsResult,
    create_lesson,
    CreateLessonResult,
    delete_lesson,
    DeleteLessonResult,
    get_lesson,
    GetLessonResult,
    update_lesson,
    UpdateLessonResult,
)
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio
