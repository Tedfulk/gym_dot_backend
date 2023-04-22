import pytest

from api.gym_dot_lib.context.facilities import (
    CreateFacilityResult,
    GetFacilityResult,
    UpdateFacilityResult,
    delete_facility,
    get_facility,
    update_facility,
)
from api.gym_dot_lib.context.main import client
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_get_facility(sample_facility: CreateFacilityResult):
    facility = await get_facility(
        executor=client,
        facility_id=sample_facility.id,
    )
    assert facility is not None
    assert facility == CreateFacilityResult(**sample_facility.dict())


async def test_update_facility(sample_facility: CreateFacilityResult):
    new_name = sample_facility.name + " (updated)"
    updates = UpdateFacilityResult(**{**sample_facility.dict(), "name": new_name})
    updated_facility = await update_facility(
        executor=client,
        facility_id=sample_facility.id,
        name=updates.name,
        address=updates.address,
        city=updates.city,
        state=updates.state,
    )
    assert updated_facility is not None
    assert CreateFacilityResult(**sample_facility.dict()) != UpdateFacilityResult(
        **updated_facility.dict()
    )


async def test_delete_facility(sample_facility: CreateFacilityResult):
    deleted_facility = await delete_facility(
        executor=client,
        facility_id=sample_facility.id,
    )
    assert deleted_facility is not None
    facility = await get_facility(
        executor=client,
        facility_id=deleted_facility.id,
    )
    assert facility is None
