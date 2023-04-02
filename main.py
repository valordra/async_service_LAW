from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from config.celery_utils import create_celery
from routers import recipes


def start_app() -> FastAPI:
    current_app = FastAPI(
        title="CuisineCruisinAPI",
        description="An asynchronous webservice using FastAPI, rabbitMQ, and celery for LAW's Individual Assignment-2\n"
                    "Browse recipes to break your fasting during holy ramadhan!"
    )
    current_app.celery_app = create_celery()
    current_app.include_router(recipes.router)
    return current_app


app = start_app()
celery = app.celery_app


@app.get("/")
async def root():
    return RedirectResponse("/docs")

