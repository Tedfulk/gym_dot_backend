import asyncio

from fastapi import APIRouter
from gym_dot_lib.context.companies import AllCompaniesResult, all_companies
from gym_dot_lib.context.main import client


app = APIRouter()


@app.get("", response_model=list[AllCompaniesResult])
def get_all_companies():
    companies = all_companies(executor=client)
    return asyncio.run(companies)
