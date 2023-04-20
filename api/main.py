import companies_api
import facilities_api
import lessons_api
import programs_api
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from httpx import AsyncClient
from utils import Tag, description, servers

app = FastAPI(
    title="Gym Dot Lib",
    description=description(Tag),
    servers=servers(),
)

ORIGINS = [
    "*",
]

async_client = AsyncClient(app=app, base_url="http://testserver")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    companies_api.app,
    prefix="/companies",
    tags=[Tag.companies],
)
app.include_router(
    facilities_api.app,
    prefix="/facilities",
    tags=[Tag.facilities],
)
app.include_router(
    programs_api.app,
    prefix="/programs",
    tags=[Tag.programs],
)
app.include_router(
    lessons_api.app,
    prefix="/lessons",
    tags=[Tag.lessons],
)
