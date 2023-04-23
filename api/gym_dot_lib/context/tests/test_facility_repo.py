import pytest

from api.gym_dot_lib.context.facilities import (
    DeleteFacilityResult,
    Facility,
    FacilityRepo,
    FacilityUpdates,
    NewFacility,
)
from api.gym_dot_lib.context.main import client
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_get_facility(sample_facility: Facility):
    facility = await FacilityRepo.get(
        executor=client,
        facility_id=sample_facility.id,
    )
    assert facility is not None
    assert facility == Facility(**sample_facility.dict())


async def test_update_facility(sample_facility: Facility):
    new_name = sample_facility.name + " (updated)"
    updates = FacilityUpdates(**{**sample_facility.dict(), "name": new_name})
    updated_facility = await FacilityRepo.update(
        executor=client,
        facility_id=sample_facility.id,
        updates=FacilityUpdates(
            name=updates.name,
            address=updates.address,
            city=updates.city,
            state=updates.state,
        ),
    )
    assert updated_facility is not None
    assert Facility(**sample_facility.dict()) != FacilityUpdates(
        **updated_facility.dict()
    )


async def test_delete_facility():
    sample_facility = await FacilityRepo.create(
        executor=client,
        new_facility=NewFacility(
            name="Sample Facility",
            address="123 Main St.",
            city="Anytown",
            state="CA",
        ),
    )
    deleted_facility = await FacilityRepo.delete(
        executor=client,
        facility_id=sample_facility.id,
    )
    assert deleted_facility is not None
    facility = await FacilityRepo.get(
        executor=client,
        facility_id=deleted_facility.id,
    )
    assert facility is None
