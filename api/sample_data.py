import asyncio
from datetime import date, time, timedelta

import pytest
from api.gym_dot_lib.context.companies import (
    CreateCompanyResult,
    DeleteCompanyResult,
    create_company,
    delete_company,
)
from api.gym_dot_lib.context.facilities import (
    CreateFacilityResult,
    DeleteFacilityResult,
    create_facility,
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


@pytest.fixture
async def sample_company():
    company = await create_company(executor=client, company_name="Sample Company")
    yield company
    await delete_company(executor=client, company_id=company.id)


@pytest.fixture
async def sample_facility1() -> CreateFacilityResult:
    return await create_facility(
        executor=client,
        name="Sample Facility",
        address="1234 Main St",
        city="Cromwell",
        state="IN",
    )


@pytest.fixture
async def sample_facility2() -> CreateFacilityResult:
    return await create_facility(
        executor=client,
        name="Sample Facility 2",
        address="4321 Main St",
        city="West Lafayette",
        state="IN",
    )


@pytest.fixture
async def sample_program() -> CreateProgramResult:
    return await create_program(
        executor=client,
        name="Sample Program",
        description="Sample Description",
        active=True,
    )


@pytest.fixture
async def sample_lesson() -> CreateLessonResult:
    return await create_lesson(
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
