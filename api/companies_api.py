import asyncio
from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.companies import (
    AllCompaniesResult,
    CreateCompanyResult,
    DeleteCompanyResult,
    GetCompanyResult,
    GetFacilitiesResult,
    RemoveFacilityResult,
    AddFacilityResult,
    UpdateCompanyResult,
    all_companies,
    create_company,
    delete_company,
    get_company,
    get_facilities,
    remove_facility,
    add_facility,
    update_company,
)
from gym_dot_lib.context.main import client

app = APIRouter()


@app.get("", response_model=list[AllCompaniesResult])
def get_all_companies():
    companies = all_companies(executor=client)
    return asyncio.run(companies)


@app.get("/{company_id}", response_model=GetCompanyResult)
def get_company_by_id(company_id: UUID):
    company = get_company(executor=client, company_id=company_id)
    return asyncio.run(company)


@app.post("", response_model=CreateCompanyResult)
def make_company(company_name: str):
    company = create_company(executor=client, company_name=company_name)
    return asyncio.run(company)


@app.put("/{company_id}", response_model=UpdateCompanyResult)
def update_company_by_id(company_id: UUID, company_name: str):
    company = update_company(
        executor=client, company_id=company_id, company_name=company_name
    )
    return asyncio.run(company)


@app.delete("/{company_id}", response_model=DeleteCompanyResult)
def delete_company_by_id(company_id: UUID):
    company = delete_company(executor=client, company_id=company_id)
    return asyncio.run(company)


@app.get("/{company_id}/facilities", response_model=list[GetFacilitiesResult])
def get_facilities_by_company_id(company_id: UUID):
    facilities = get_facilities(executor=client, company_id=company_id)
    return asyncio.run(facilities)


@app.put("/{company_id}/facilities", response_model=AddFacilityResult)
def add_facility_to_company(company_id: UUID, facility_id: UUID):
    facility = add_facility(
        executor=client, company_id=company_id, facility_id=facility_id
    )
    return asyncio.run(facility)


@app.put("/{company_id}facilities", response_model=RemoveFacilityResult)
def remove_facility_from_company(company_id: UUID, facility_id: UUID):
    facility = remove_facility(
        executor=client, company_id=company_id, facility_id=facility_id
    )
    return asyncio.run(facility)
