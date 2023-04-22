import pytest

from api.gym_dot_lib.context.facilities.programs.lessons import (
    AllLessonsResult,
    CreateLessonResult,
    DeleteLessonResult,
    GetLessonResult,
    UpdateLessonResult,
    all_lessons,
    create_lesson,
    delete_lesson,
    get_lesson,
    update_lesson,
)
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio
