import pytest

from api.gym_dot_lib.context.facilities.programs import (
    AddLessonResult,
    AllProgramsResult,
    CreateProgramResult,
    CreateProgramWithLessonResult,
    DeleteProgramResult,
    GetLessonsResult,
    GetProgramResult,
    RemoveLessonResult,
    UpdateProgramResult,
    add_lesson,
    all_programs,
    create_program,
    create_program_with_lesson,
    delete_program,
    get_lessons,
    get_program,
    remove_lesson,
    update_program,
)
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio
