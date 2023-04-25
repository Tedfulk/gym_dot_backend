"""
Contains fixtures for unit/(repo) and end-to-end/(api) test.
"""
import asyncio
from datetime import date, time, timedelta

import pytest

from api.gym_dot_lib.context.companies import CompanyRepo, NewCompany
from api.gym_dot_lib.context.facilities import FacilityRepo, NewFacility
from api.gym_dot_lib.context.facilities.programs import NewProgram, ProgramRepo
from api.gym_dot_lib.context.facilities.programs.lessons import LessonRepo, NewLesson
from api.gym_dot_lib.context.main import client


@pytest.fixture(scope="session")
def event_loop():
    """Force the pytest-asyncio loop to be the main one."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def sample_company():
    company = await CompanyRepo.create(
        executor=client, new_company=NewCompany(name="Sample Company")
    )
    if company is not None:
        yield company
    await CompanyRepo.delete(executor=client, company_id=company.id)


@pytest.fixture
async def sample_company_with_facility():
    company = await CompanyRepo.create_company_and_facility(
        executor=client,
        new_company=NewCompany(name="Sample Company"),
        new_facility=NewFacility(
            name="Sample Facility",
            address="1234 Main St",
            city="Cromwell",
            state="IN",
        ),
    )
    if company is not None:
        yield company
    await CompanyRepo.delete(executor=client, company_id=company.id)


@pytest.fixture
async def sample_facility():
    facility = await FacilityRepo.create(
        executor=client,
        new_facility=NewFacility(
            name="Sample Facility",
            address="1234 Main St",
            city="Cromwell",
            state="IN",
        ),
    )
    if facility is not None:
        yield facility
    await FacilityRepo.delete(executor=client, facility_id=facility.id)


@pytest.fixture
async def sample_facility2():
    facility = await FacilityRepo.create(
        executor=client,
        new_facility=NewFacility(
            name="Another Facility",
            address="555 Main St",
            city="Ligonier",
            state="IN",
        ),
    )
    if facility is not None:
        yield facility
    await FacilityRepo.delete(executor=client, facility_id=facility.id)


@pytest.fixture
async def sample_program():
    program = await ProgramRepo.create(
        executor=client,
        new_program=NewProgram(
            name="Sample Program",
            description="Sample Description",
            active=True,
        ),
    )
    if program is not None:
        yield program
    await ProgramRepo.delete(executor=client, program_id=program.id)


@pytest.fixture
async def sample_lesson():
    lesson = await LessonRepo.create(
        executor=client,
        new_lesson=NewLesson(
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
        ),
    )
    if lesson is not None:
        yield lesson
    await LessonRepo.delete(executor=client, lesson_id=lesson.id)


@pytest.fixture
async def sample_program_with_lesson():
    program_with_lesson = await ProgramRepo.create_program_with_lesson(
        executor=client,
        new_program=NewProgram(
            name="Sample Program",
            description="Sample Description",
        ),
        new_lesson=NewLesson(
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
            max_attendees=20,
            min_attendees=1,
            waitlist=10,
        ),
    )
    if program_with_lesson is not None:
        yield program_with_lesson
    await ProgramRepo.delete(executor=client, program_id=program_with_lesson.id)
