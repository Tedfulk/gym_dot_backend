import pytest

from api.gym_dot_lib.context.companies import (
    Company,
    CompanyUpdates,
    CompanyWithFacilities,
    DeleteCompanyResult,
    NewCompany,
)
from api.gym_dot_lib.context.facilities import Facility
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


async def test_get_company_by_id(sample_company: Company):
    """GET /companies/{company_id}"""
    response = await AC.get(f"/companies/{sample_company.id}")
    assert response.status_code == 200
    assert Company(**response.json()) == sample_company.dict()


async def test_post_company():
    """POST /companies"""
    new_company = NewCompany(name="Test Company")
    resp = await AC.post("/companies", data=new_company.json())
    company = await AC.get(f"/companies/{resp.json()['id']}")
    assert resp.status_code == 200
    assert resp.json() == company.json()
    await AC.delete(f"/companies/{resp.json()['id']}")


async def test_put_company_by_id(sample_company: Company):
    """PUT /companies/{company_id}"""
    updates = CompanyUpdates(name=sample_company.name + "(Updated)")
    updated_company = await AC.put(
        f"/companies/{sample_company.id}",
        data=updates.json(),
    )
    updated_company_id = updated_company.json()["id"]
    company = await AC.get(f"/companies/{updated_company_id}")
    assert updated_company.status_code == 200
    assert updated_company.json() == company.json()


async def test_delete_company_by_id():
    """DELETE /companies/{company_id}"""
    new_company = NewCompany(name="Test Company")
    resp = await AC.post("/companies", data=new_company.json())
    deleted_company = await AC.delete(f"/companies/{resp.json()['id']}")
    assert deleted_company.status_code == 200
    assert DeleteCompanyResult(**deleted_company.json()) == DeleteCompanyResult(
        **resp.json()
    )


async def test_get_facilities_by_company_id(sample_company: Company):
    """GET /companies/{company_id}/facilities"""
    response = await AC.get(f"/companies/{sample_company.id}/facilities")
    assert response.status_code == 200
    assert CompanyWithFacilities(**response.json())


async def test_add_facility_to_company(
    sample_company: Company, sample_facility: Facility
):
    """PUT /companies/{company_id}/add/facilities"""
    response = await AC.put(
        f"/companies/{sample_company.id}/add/facilities?facility_id={sample_facility.id}",
    )
    company = await AC.get(f"/companies/{response.json()['id']}")
    assert response.status_code == 200
    assert Company(**response.json()) == Company(**company.json())


async def test_remove_facility_from_company(
    sample_company: Company, sample_facility: Facility
):
    """PUT /companies/{company_id}/remove/facilities"""
    response = await AC.put(
        f"/companies/{sample_company.id}/remove/facilities?facility_id={sample_facility.id}",
    )
    company = await AC.get(f"/companies/{response.json()['id']}")
    assert response.status_code == 200
    assert Company(**response.json()) == Company(**company.json())
