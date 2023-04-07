import asyncio
from fastapi import FastAPI
from gym_dot_lib.context.main import client
from gym_dot_lib.context.companies import all_companies

# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "*",
]


@app.get("/{companies}")
async def get_all_companies():
    companies = all_companies(executor=client)
    return asyncio.run(companies)
