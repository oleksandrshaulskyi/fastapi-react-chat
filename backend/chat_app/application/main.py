from contextlib import asynccontextmanager

from application.settings import settings
from fastapi import FastAPI
print(settings)

application = FastAPI()
