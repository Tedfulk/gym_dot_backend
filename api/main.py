from fastapi import FastAPI
from utils import description, Tag, servers
from fastapi.middleware.cors import CORSMiddleware
import companies_api


app = FastAPI(
    title="Gym Dot Lib",
    description=description(Tag),
    servers=servers(),
)

ORIGINS = [
    "*",
]

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
