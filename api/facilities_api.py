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
async def get_all_facilities():
    return await all_facilities(executor=client)


@app.get("/{facility_id}", response_model=GetFacilityResult)
async def get_facility_by_id(facility_id: UUID):
    return await get_facility(executor=client, facility_id=facility_id)


@app.post("", response_model=CreateFacilityResult)
async def make_facility(name: str, address: str, city: str, state: str):
    return await create_facility(
        executor=client, name=name, address=address, city=city, state=state
    )


@app.put("/{facility_id}", response_model=UpdateFacilityResult)
async def update_facility_by_id(
    facility_id: UUID, name: str, address: str, city: str, state: str
):
    return await update_facility(
        executor=client,
        facility_id=facility_id,
        name=name,
        address=address,
        city=city,
        state=state,
    )


@app.delete("/{facility_id}", response_model=DeleteFacilityResult)
async def delete_facility_by_id(facility_id: UUID):
    return await delete_facility(executor=client, facility_id=facility_id)
