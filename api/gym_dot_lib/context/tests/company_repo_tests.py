import pytest

from api.gym_dot_lib.context.companies import (
    AllCompaniesResult,
    CreateCompanyResult,
    DeleteCompanyResult,
    GetCompanyResult,
    UpdateCompanyResult,
    all_companies,
    create_company,
    delete_company,
    get_company,
    update_company,
)
from api.gym_dot_lib.context.main import client

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# async def test_all_companies():
#     companies = await all_companies(executor=client)
#     assert companies is not None


# async def test_get_company(sample_company: CreateCompanyResult):
#     company = await get_company(executor=client, company_id=sample_company.id)
#     assert sample_company is not None
#     if company is not None:
#         assert company.id == sample_company.id


# async def test_create_company():
#     new_company = await create_company(
#         executor=client, company_name="Sample Company 2.0"
#     )
#     company = await get_company(executor=client, company_id=new_company.id)
#     assert new_company is not None
#     if company is not None:
#         assert company.id == new_company.id
#     await delete_company(executor=client, company_id=new_company.id)


# async def test_update_company(sample_company: CreateCompanyResult):
#     updated_company = await update_company(
#         executor=client,
#         company_id=sample_company.id,
#         company_name=sample_company.name + " (updated)",
#     )
#     assert updated_company is not None
#     company = await get_company(executor=client, company_id=updated_company.id)
#     if company is not None:
#         assert company.id == updated_company.id
#         assert sample_company.name != updated_company.name


async def test_delete_company(sample_company: CreateCompanyResult):
    deleted_company = await delete_company(
        executor=client, company_id=sample_company.id
    )
    assert deleted_company is not None
    company = await get_company(executor=client, company_id=deleted_company.id)
    assert company is None
