from uuid import UUID

from fastapi import APIRouter
from gym_dot_lib.context.facilities import (
    DeleteFacilityResult,
    Facility,
    FacilityRepo,
    FacilityUpdates,
    NewFacility,
)
from gym_dot_lib.context.main import client

app = APIRouter()


@app.get("", response_model=list[Facility])
async def get_all_facilities():
    return await FacilityRepo.all_facilities(executor=client)


@app.get("/{facility_id}", response_model=Facility)
async def get_facility_by_id(facility_id: UUID):
    return await FacilityRepo.get(executor=client, facility_id=facility_id)


@app.post("", response_model=Facility)
async def post_facility(new_facility: NewFacility):
    return await FacilityRepo.create(
        executor=client,
        new_facility=NewFacility(
            name=new_facility.name,
            address=new_facility.address,
            city=new_facility.city,
            state=new_facility.state,
        ),
    )


@app.put("/{facility_id}", response_model=Facility)
async def put_facility_by_id(
    facility_id: UUID,
    updates: FacilityUpdates,
):
    return await FacilityRepo.update(
        executor=client,
        facility_id=facility_id,
        updates=FacilityUpdates(
            name=updates.name,
            address=updates.address,
            city=updates.city,
            state=updates.state,
        ),
    )


@app.delete("/{facility_id}", response_model=DeleteFacilityResult)
async def delete_facility_by_id(facility_id: UUID):
    return await FacilityRepo.delete(executor=client, facility_id=facility_id)
