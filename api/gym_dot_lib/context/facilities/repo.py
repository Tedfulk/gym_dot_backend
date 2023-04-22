import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import parse_raw_as

from .models import DeleteFacilityResult, Facility, FacilityUpdates, NewFacility
from .queries import (
    ALL_FACILITIES,
    CREATE_FACILITY,
    DELETE_FACILITY,
    GET_FACILITY,
    UPDATE_FACILITY,
)


class FacilityRepo:
    """Methods for Company entity in EdgeDB."""

    @staticmethod
    async def get(
        executor: AsyncIOExecutor,
        *,
        facility_id: UUID,
    ) -> Facility | None:
        resp = await executor.query_single_json(
            GET_FACILITY,
            facility_id=facility_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Facility | None, resp, json_loads=orjson.loads
        )
        return cast(Facility | None, parsed)

    @staticmethod
    async def create(
        executor: AsyncIOExecutor,
        *,
        new_facility: NewFacility,
    ) -> Facility:
        resp = await executor.query_single_json(
            CREATE_FACILITY,
            name=new_facility.name,
            address=new_facility.address,
            city=new_facility.city,
            state=new_facility.state,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Facility, resp, json_loads=orjson.loads
        )
        return cast(Facility, parsed)

    @staticmethod
    async def update(
        executor: AsyncIOExecutor,
        *,
        facility_id: UUID,
        updates: FacilityUpdates,
    ) -> Facility | None:
        resp = await executor.query_single_json(
            UPDATE_FACILITY,
            facility_id=facility_id,
            name=updates.name,
            address=updates.address,
            city=updates.city,
            state=updates.state,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Facility | None, resp, json_loads=orjson.loads
        )
        return cast(Facility | None, parsed)

    @staticmethod
    async def delete(
        executor: AsyncIOExecutor,
        *,
        facility_id: UUID,
    ) -> DeleteFacilityResult:
        resp = await executor.query_single_json(
            DELETE_FACILITY,
            facility_id=facility_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, DeleteFacilityResult, resp, json_loads=orjson.loads
        )
        return cast(DeleteFacilityResult, parsed)

    @staticmethod
    async def all_facilities(
        executor: AsyncIOExecutor,
    ) -> list[Facility]:
        resp = await executor.query_json(
            ALL_FACILITIES,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, list[Facility], resp, json_loads=orjson.loads
        )
        return cast(list[Facility], parsed)
