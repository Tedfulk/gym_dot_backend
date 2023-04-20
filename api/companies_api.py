from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.companies import (
    AddFacilityResult,
    AllCompaniesResult,
    CreateCompanyResult,
    DeleteCompanyResult,
    GetCompanyResult,
    GetFacilitiesResult,
    RemoveFacilityResult,
    UpdateCompanyResult,
    add_facility,
    all_companies,
    create_company,
    delete_company,
    get_company,
    get_facilities,
    remove_facility,
    update_company,
)
from gym_dot_lib.context.main import client

app = APIRouter()


@app.get("", response_model=list[AllCompaniesResult])
async def get_all_companies():
    return await all_companies(executor=client)


@app.get("/{company_id}", response_model=GetCompanyResult)
async def get_company_by_id(company_id: UUID):
    return await get_company(executor=client, company_id=company_id)


@app.post("", response_model=CreateCompanyResult)
async def post_company(company_name: str):
    return await create_company(executor=client, company_name=company_name)


@app.put("/{company_id}", response_model=UpdateCompanyResult)
async def put_company_by_id(company_id: UUID, company_name: str):
    return await update_company(
        executor=client, company_id=company_id, company_name=company_name
    )


@app.delete("/{company_id}", response_model=DeleteCompanyResult)
async def delete_company_by_id(company_id: UUID):
    return await delete_company(executor=client, company_id=company_id)


@app.get("/{company_id}/facilities", response_model=GetFacilitiesResult)
async def get_facilities_by_company_id(company_id: UUID):
    return await get_facilities(executor=client, company_id=company_id)


@app.put("/{company_id}/add/facilities", response_model=AddFacilityResult)
async def add_facility_to_company(company_id: UUID, facility_id: UUID):
    return await add_facility(
        executor=client, company_id=company_id, facility_id=facility_id
    )


@app.put("/{company_id}/remove/facilities", response_model=RemoveFacilityResult)
async def remove_facility_from_company(company_id: UUID, facility_id: UUID):
    return await remove_facility(
        executor=client, company_id=company_id, facility_id=facility_id
    )
