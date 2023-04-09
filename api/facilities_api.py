import asyncio
from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.facilities import (
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
from gym_dot_lib.context.main import client

app = APIRouter()


@app.get("", response_model=list[AllFacilitiesResult])
def get_all_facilities():
    facilities = all_facilities(executor=client)
    return asyncio.run(facilities)


@app.get("/{facility_id}", response_model=GetFacilityResult)
def get_facility_by_id(facility_id: UUID):
    facility = get_facility(executor=client, facility_id=facility_id)
    return asyncio.run(facility)


@app.post("", response_model=CreateFacilityResult)
def make_facility(name: str, address: str, city: str, state: str):
    facility = create_facility(
        executor=client, name=name, address=address, city=city, state=state
    )
    return asyncio.run(facility)


@app.put("/{facility_id}", response_model=UpdateFacilityResult)
def update_facility_by_id(
    facility_id: UUID, name: str, address: str, city: str, state: str
):
    facility = update_facility(
        executor=client,
        facility_id=facility_id,
        name=name,
        address=address,
        city=city,
        state=state,
    )
    return asyncio.run(facility)


@app.delete("/{facility_id}", response_model=DeleteFacilityResult)
def delete_facility_by_id(facility_id: UUID):
    facility = delete_facility(executor=client, facility_id=facility_id)
    return asyncio.run(facility)
