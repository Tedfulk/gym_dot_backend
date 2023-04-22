import pytest

from api.gym_dot_lib.context.companies import (
    AddFacilityResult,
    CreateCompanyResult,
    DeleteCompanyResult,
    GetFacilitiesResult,
    RemoveFacilityResult,
)
from api.gym_dot_lib.context.facilities import CreateFacilityResult
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_get_all_companies():
    """GET /companies"""
    response = await AC.get("/companies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


async def test_get_company_by_id(sample_company: CreateCompanyResult):
    """GET /companies/{company_id}"""
    response = await AC.get(f"/companies/{sample_company.id}")
    assert response.status_code == 200
    assert CreateCompanyResult(**response.json()) == sample_company.dict()


async def test_post_company():
    """POST /companies"""
    company_name = "Test Company"
    new_company = await AC.post(
        f"/companies?company_name={company_name}", json={"company_name": company_name}
    )
    new_company_id = new_company.json()["id"]
    company = await AC.get(f"/companies/{new_company_id}")
    assert new_company.status_code == 200
    assert new_company.json() == company.json()


async def test_put_company_by_id(sample_company: CreateCompanyResult):
    """PUT /companies/{company_id}"""
    new_company_name = sample_company.name + "(Updated)"
    updated_company = await AC.put(
        f"/companies/{sample_company.id}?company_name={new_company_name}",
        json={"company_name": new_company_name},
    )
    updated_company_id = updated_company.json()["id"]
    company = await AC.get(f"/companies/{updated_company_id}")
    assert updated_company.status_code == 200
    assert updated_company.json() == company.json()


async def test_delete_company_by_id(sample_company: CreateCompanyResult):
    """DELETE /companies/{company_id}"""
    deleted_company = await AC.delete(f"/companies/{sample_company.id}")
    assert deleted_company.status_code == 200
    assert DeleteCompanyResult(**deleted_company.json()) == DeleteCompanyResult(
        **sample_company.dict()
    )


async def test_get_facilities_by_company_id(sample_company: CreateCompanyResult):
    """GET /companies/{company_id}/facilities"""
    response = await AC.get(f"/companies/{sample_company.id}/facilities")
    assert response.status_code == 200
    assert GetFacilitiesResult(**response.json())


async def test_add_facility_to_company(
    sample_company: CreateCompanyResult, sample_facility: CreateFacilityResult
):
    """PUT /companies/{company_id}/add/facilities"""
    response = await AC.put(
        f"/companies/{sample_company.id}/add/facilities?facility_id={sample_facility.id}",
    )
    company = await AC.get(f"/companies/{response.json()['id']}")
    assert response.status_code == 200
    assert AddFacilityResult(**response.json()) == AddFacilityResult(**company.json())
    await AC.delete(f"/companies/{response.json()['id']}")


async def test_remove_facility_from_company(
    sample_company: CreateCompanyResult, sample_facility: CreateFacilityResult
):
    """PUT /companies/{company_id}/remove/facilities"""
    response = await AC.put(
        f"/companies/{sample_company.id}/remove/facilities?facility_id={sample_facility.id}",
    )
    company = await AC.get(f"/companies/{response.json()['id']}")
    assert response.status_code == 200
    assert RemoveFacilityResult(**response.json()) == RemoveFacilityResult(
        **company.json()
    )
