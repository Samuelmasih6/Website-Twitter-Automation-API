from fastapi import FastAPI
from app.api import ingest

app = FastAPI(title="Website to Twitter API")

app.include_router(ingest.router)
