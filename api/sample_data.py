import asyncio
from datetime import date, time, timedelta

import pytest

from api.gym_dot_lib.context.companies import (
    CreateCompanyAndFacilityResult,
    CreateCompanyResult,
    DeleteCompanyResult,
    create_company,
    create_company_and_facility,
    delete_company,
)
from api.gym_dot_lib.context.facilities import (
    CreateFacilityResult,
    DeleteFacilityResult,
    create_facility,
    delete_facility,
)
from api.gym_dot_lib.context.facilities.programs import (
    CreateProgramResult,
    DeleteProgramResult,
    create_program,
    delete_program,
)
from api.gym_dot_lib.context.facilities.programs.lessons import (
    CreateLessonResult,
    DeleteLessonResult,
    create_lesson,
    delete_lesson,
)
from api.gym_dot_lib.context.main import client


@pytest.fixture(scope="session")
def event_loop():
    """Force the pytest-asyncio loop to be the main one."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def sample_company():
    company = await create_company(executor=client, company_name="Sample Company")
    if company is not None:
        yield company
    await delete_company(executor=client, company_id=company.id)


@pytest.fixture
async def sample_company_with_facility():
    company = await create_company_and_facility(
        executor=client,
        company_name="Sample Company",
        facility_name="Sample Facility",
        address="1234 Main St",
        city="Cromwell",
        state="IN",
    )
    if company is not None:
        yield company
    await delete_company(executor=client, company_id=company.id)


@pytest.fixture
async def sample_facility1():
    facility = await create_facility(
        executor=client,
        name="Sample Facility",
        address="1234 Main St",
        city="Cromwell",
        state="IN",
    )
    if facility is not None:
        yield facility
    await delete_facility(executor=client, facility_id=facility.id)


@pytest.fixture
async def sample_facility2():
    facility = await create_facility(
        executor=client,
        name="Sample Facility 2",
        address="4321 Main St",
        city="West Lafayette",
        state="IN",
    )
    if facility is not None:
        yield facility
    await delete_facility(executor=client, facility_id=facility.id)


@pytest.fixture
async def sample_program():
    program = await create_program(
        executor=client,
        name="Sample Program",
        description="Sample Description",
        active=True,
    )
    if program is not None:
        yield program
    await delete_program(executor=client, program_id=program.id)


@pytest.fixture
async def sample_lesson():
    lesson = await create_lesson(
        executor=client,
        class_dates=[
            date.today(),
            date.today() + timedelta(days=1),
            date.today() + timedelta(days=2),
        ],
        class_times=[
            time(6, 0),
            time(9, 30),
            time(12, 0),
            time(16, 30),
            time(17, 30),
            time(18, 30),
        ],
        len_of_class_time=60,
        active=True,
        max_attendees=20,
        min_attendees=1,
        waitlist=10,
    )
    if lesson is not None:
        yield lesson
    await delete_lesson(executor=client, lesson_id=lesson.id)
