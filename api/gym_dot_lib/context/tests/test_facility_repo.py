import pytest

from api.gym_dot_lib.context.facilities import (
    CreateFacilityResult,
    DeleteFacilityResult,
    GetFacilityResult,
    UpdateFacilityResult,
    create_facility,
    delete_facility,
    get_facility,
    update_facility,
)
from api.gym_dot_lib.context.main import client
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_get_facility(sample_facility1: CreateFacilityResult):
    facility = await get_facility(
        executor=client,
        facility_id=sample_facility1.id,
    )
    assert facility is not None
    assert facility == CreateFacilityResult(**sample_facility1.dict())


async def test_create_facility():
    new_facility = await create_facility(
        executor=client,
        name="Sample Facility 2.0",
        address="1234 Sample St",
        city="Sample City",
        state="NC",
    )
    facility = await get_facility(
        executor=client,
        facility_id=new_facility.id,
    )
    assert new_facility is not None
    if facility is not None:
        assert GetFacilityResult(**facility.dict()) == CreateFacilityResult(
            **new_facility.dict()
        )
    await delete_facility(
        executor=client,
        facility_id=new_facility.id,
    )


async def test_update_facility(sample_facility1: CreateFacilityResult):
    new_name = sample_facility1.name + " (updated)"
    updates = UpdateFacilityResult(**{**sample_facility1.dict(), "name": new_name})
    updated_facility = await update_facility(
        executor=client,
        facility_id=sample_facility1.id,
        name=updates.name,
        address=updates.address,
        city=updates.city,
        state=updates.state,
    )
    assert updated_facility is not None
    assert CreateFacilityResult(**sample_facility1.dict()) != UpdateFacilityResult(
        **updated_facility.dict()
    )


async def test_delete_facility(sample_facility1: CreateFacilityResult):
    deleted_facility = await delete_facility(
        executor=client,
        facility_id=sample_facility1.id,
    )
    assert deleted_facility is not None
    facility = await get_facility(
        executor=client,
        facility_id=deleted_facility.id,
    )
    assert facility is None
