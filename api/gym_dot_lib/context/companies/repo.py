import asyncio
from typing import cast
from uuid import UUID

import orjson
from edgedb import AsyncIOExecutor
from pydantic import parse_raw_as

from gym_dot_lib.context.facilities import NewFacility

from .models import (
    Company,
    CompanyUpdates,
    CompanyWithFacilities,
    DeleteCompanyResult,
    NewCompany,
)
from .queries import (
    ADD_FACILITY,
    ALL_COMPANIES,
    CREATE_COMPANY,
    CREATE_COMPANY_AND_FACILTY,
    DELETE_COMPANY,
    GET_COMPANY,
    GET_FACILITIES,
    REMOVE_FACILITY,
    UPDATE_COMPANY,
)


class CompanyRepo:
    """Methods for Company entity in EdgeDB."""

    @staticmethod
    async def get(
        executor: AsyncIOExecutor,
        *,
        company_id: UUID,
    ) -> Company | None:
        resp = await executor.query_single_json(
            GET_COMPANY,
            company_id=company_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Company | None, resp, json_loads=orjson.loads
        )
        return cast(Company | None, parsed)

    @staticmethod
    async def create(
        executor: AsyncIOExecutor,
        *,
        new_company: NewCompany,
    ) -> Company:
        resp = await executor.query_single_json(
            CREATE_COMPANY,
            company_name=new_company.name,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Company, resp, json_loads=orjson.loads
        )
        return cast(Company, parsed)

    @staticmethod
    async def update(
        executor: AsyncIOExecutor,
        *,
        company_id: UUID,
        updates: CompanyUpdates,
    ) -> Company:
        resp = await executor.query_single_json(
            UPDATE_COMPANY,
            company_id=company_id,
            company_name=updates.name,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Company, resp, json_loads=orjson.loads
        )
        return cast(Company, parsed)

    @staticmethod
    async def delete(
        executor: AsyncIOExecutor,
        *,
        company_id: UUID,
    ) -> DeleteCompanyResult:
        resp = await executor.query_single_json(
            DELETE_COMPANY,
            company_id=company_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, DeleteCompanyResult, resp, json_loads=orjson.loads
        )
        return cast(DeleteCompanyResult, parsed)

    @staticmethod
    async def add_facility(
        executor: AsyncIOExecutor,
        *,
        company_id: UUID,
        facility_id: UUID,
    ) -> Company:
        resp = await executor.query_single_json(
            ADD_FACILITY,
            company_id=company_id,
            facility_id=facility_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Company, resp, json_loads=orjson.loads
        )
        return cast(Company, parsed)

    @staticmethod
    async def remove_facility(
        executor: AsyncIOExecutor,
        *,
        company_id: UUID,
        facility_id: UUID,
    ) -> Company:
        resp = await executor.query_single_json(
            REMOVE_FACILITY,
            company_id=company_id,
            facility_id=facility_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, Company, resp, json_loads=orjson.loads
        )
        return cast(Company, parsed)

    # might fail, need to test
    @staticmethod
    async def create_company_and_facility(
        executor: AsyncIOExecutor, *, new_company: NewCompany, new_facility: NewFacility
    ) -> CompanyWithFacilities:
        resp = await executor.query_single_json(
            CREATE_COMPANY_AND_FACILTY,
            company_name=new_company.name,
            facility_name=new_facility.name,
            address=new_facility.address,
            city=new_facility.city,
            state=new_facility.state,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, CompanyWithFacilities, resp, json_loads=orjson.loads
        )
        return cast(CompanyWithFacilities, parsed)

    @staticmethod
    async def all_companies(
        executor: AsyncIOExecutor,
    ) -> list[Company]:
        resp = await executor.query_json(
            ALL_COMPANIES,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, list[Company], resp, json_loads=orjson.loads
        )
        return cast(list[Company], parsed)

    @staticmethod
    async def get_facilities(
        executor: AsyncIOExecutor,
        *,
        company_id: UUID,
    ) -> CompanyWithFacilities | None:
        resp = await executor.query_single_json(
            GET_FACILITIES,
            company_id=company_id,
        )
        parsed = await asyncio.to_thread(
            parse_raw_as, CompanyWithFacilities | None, resp, json_loads=orjson.loads
        )
        return cast(CompanyWithFacilities | None, parsed)
