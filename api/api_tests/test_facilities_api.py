import pytest

from api.gym_dot_lib.context.facilities import (
    AllFacilitiesResult,
    CreateFacilityResult,
    DeleteFacilityResult,
    GetFacilityResult,
    UpdateFacilityResult,
    all_facilities,
    create_facility,
    delete_facility,
    get_facility,
    update_facility,
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


async def test_get_facility_by_id(sample_facility: CreateFacilityResult):
    """GET /facilities/{facility_id}"""
    response = await AC.get(f"/facilities/{sample_facility.id}")
    assert response.status_code == 200
    assert GetFacilityResult(**response.json()) == sample_facility.dict()


async def test_post_facility():
    """POST /facilities"""
    facility_dict = {
        "name": "Sample Facility",
        "address": "1234 Main St",
        "city": "Cromwell",
        "state": "IN",
    }
    new_facility = await AC.post(
        f"/facilities",
        json={**facility_dict},
    )
    print(new_facility.json())
    assert new_facility.status_code == 200
    new_facility_id = new_facility.json()
    facility = await AC.get(f"/facilities/{new_facility_id}")
    assert new_facility.status_code == 200
    assert new_facility.json() == facility.json()
