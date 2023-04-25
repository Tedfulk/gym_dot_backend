import pytest

from api.gym_dot_lib.context.facilities import (
    DeleteFacilityResult,
    Facility,
    FacilityUpdates,
    NewFacility,
)
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_get_all_facilities():
    """GET /facilities"""
    response = await AC.get("/facilities")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


async def test_get_facility_by_id(sample_facility: Facility):
    """GET /facilities/{facility_id}"""
    response = await AC.get(f"/facilities/{sample_facility.id}")
    assert response.status_code == 200
    assert Facility(**response.json()) == sample_facility.dict()


async def test_post_facility():
    """POST /facilities"""
    new_facility = NewFacility(
        name="Sample Facility",
        address="1234 Main St",
        city="Cromwell",
        state="IN",
    )
    resp = await AC.post(
        "/facilities",
        data=new_facility.json(),
    )
    assert resp.status_code == 200
    new_facility_id = resp.json()["id"]
    facility = await AC.get(f"/facilities/{new_facility_id}")
    assert resp.json() == facility.json()
    await AC.delete(f"/facilities/{new_facility_id}")


async def test_put_facility_by_id(sample_facility: Facility):
    """PUT /facilities/{facility_id}"""
    updates = FacilityUpdates(
        **{**sample_facility.dict(), "name": sample_facility.name + "(Updated)"}
    )
    updated_facility = await AC.put(
        f"/facilities/{sample_facility.id}",
        data=updates.json(),
    )
    updated_facility_id = updated_facility.json()["id"]
    facility = await AC.get(f"/facilities/{updated_facility_id}")
    assert updated_facility.status_code == 200
    assert Facility(**updated_facility.json()) == Facility(**facility.json())


async def test_delete_facility():
    """DELETE /facilities/{facility_id}"""
    new_facility = NewFacility(
        name="Sample Facility",
        address="1234 Main St",
        city="Cromwell",
        state="IN",
    )
    resp = await AC.post(
        "/facilities",
        data=new_facility.json(),
    )
    deleted_facility = await AC.delete(f"/facilities/{resp.json()['id']}")
    assert deleted_facility.status_code == 200
    assert DeleteFacilityResult(**deleted_facility.json()) == DeleteFacilityResult(
        **resp.json()
    )
