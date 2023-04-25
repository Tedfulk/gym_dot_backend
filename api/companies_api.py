from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.companies import (
    Company,
    CompanyRepo,
    CompanyUpdates,
    CompanyWithFacilities,
    DeleteCompanyResult,
    NewCompany,
)
from gym_dot_lib.context.main import client

app = APIRouter()


@app.get("", response_model=list[Company])
async def get_all_companies():
    return await CompanyRepo.all_companies(executor=client)


@app.get("/{company_id}", response_model=Company)
async def get_company_by_id(company_id: UUID):
    return await CompanyRepo.get(executor=client, company_id=company_id)


@app.post("", response_model=Company)
async def post_company(new_company: NewCompany):
    return await CompanyRepo.create(executor=client, new_company=new_company)


@app.put("/{company_id}", response_model=Company)
async def put_company_by_id(company_id: UUID, updates: CompanyUpdates):
    return await CompanyRepo.update(
        executor=client, company_id=company_id, updates=updates
    )


@app.delete("/{company_id}", response_model=DeleteCompanyResult)
async def delete_company_by_id(company_id: UUID):
    return await CompanyRepo.delete(executor=client, company_id=company_id)


@app.get("/{company_id}/facilities", response_model=CompanyWithFacilities)
async def get_facilities_by_company_id(company_id: UUID):
    return await CompanyRepo.get_facilities(executor=client, company_id=company_id)


@app.put("/{company_id}/add/facilities", response_model=Company)
async def add_facility_to_company(company_id: UUID, facility_id: UUID):
    return await CompanyRepo.add_facility(
        executor=client, company_id=company_id, facility_id=facility_id
    )


@app.put("/{company_id}/remove/facilities", response_model=Company)
async def remove_facility_from_company(company_id: UUID, facility_id: UUID):
    return await CompanyRepo.remove_facility(
        executor=client, company_id=company_id, facility_id=facility_id
    )
