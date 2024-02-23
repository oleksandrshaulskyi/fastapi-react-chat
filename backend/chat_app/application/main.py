from contextlib import asynccontextmanager

from fastapi import FastAPI

from application.database import create_unique_index


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_unique_index()
    yield


application = FastAPI(lifespan=lifespan)
