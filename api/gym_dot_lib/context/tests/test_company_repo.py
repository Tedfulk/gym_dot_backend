import pytest

from api.gym_dot_lib.context.companies import (
    Company,
    CompanyRepo,
    CompanyUpdates,
    CompanyWithFacilities,
    DeleteCompanyResult,
    NewCompany,
)
from api.gym_dot_lib.context.main import client

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_all_companies():
    companies = await CompanyRepo.all_companies(executor=client)
    assert companies is not None


async def test_get_company(sample_company: Company):
    company = await CompanyRepo.get(executor=client, company_id=sample_company.id)
    assert sample_company is not None
    if company is not None:
        assert company.id == sample_company.id


async def test_create_company():
    new_company = await CompanyRepo.create(
        executor=client, new_company=NewCompany(name="Sample Company 2.0")
    )
    company = await CompanyRepo.get(executor=client, company_id=new_company.id)
    assert new_company is not None
    if company is not None:
        assert company.id == new_company.id
    await CompanyRepo.delete(executor=client, company_id=new_company.id)


async def test_update_company(sample_company: Company):
    updated_company = await CompanyRepo.update(
        executor=client,
        company_id=sample_company.id,
        updates=CompanyUpdates(name=sample_company.name + " (updated)"),
    )
    assert updated_company is not None
    company = await CompanyRepo.get(executor=client, company_id=updated_company.id)
    if company is not None:
        assert company.id == updated_company.id
        assert sample_company.name != updated_company.name


async def test_delete_company():
    company = await CompanyRepo.create(
        executor=client, new_company=NewCompany(name="Sample Company")
    )
    deleted_company = await CompanyRepo.delete(executor=client, company_id=company.id)
    assert deleted_company is not None


async def test_get_facilities(sample_company_with_facility: CompanyWithFacilities):
    facilities = await CompanyRepo.get_facilities(
        executor=client, company_id=sample_company_with_facility.id
    )
    if facilities is not None:
        assert facilities == CompanyWithFacilities(
            **sample_company_with_facility.dict()
        )
