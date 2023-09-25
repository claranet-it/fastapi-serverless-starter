from fastapi import FastAPI

from fastapi_serverless_starter.routers import health

app = FastAPI()


app.include_router(health.router)
