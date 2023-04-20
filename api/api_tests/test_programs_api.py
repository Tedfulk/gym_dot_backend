import pytest

from api.gym_dot_lib.context.facilities.programs import (
    all_programs,
    AllProgramsResult,
    create_program,
    CreateProgramResult,
    delete_program,
    DeleteProgramResult,
    get_program,
    GetProgramResult,
    update_program,
    UpdateProgramResult,
    get_lessons,
    GetLessonsResult,
    add_lesson,
    AddLessonResult,
    remove_lesson,
    RemoveLessonResult,
    create_program_with_lesson,
    CreateProgramWithLessonResult,
)
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio
