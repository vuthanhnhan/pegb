from fastapi import FastAPI, Response, Request
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi
from dotenv import load_dotenv

load_dotenv()

import app.api.v1.users.controller as users

app = FastAPI()

import debugpy
debugpy.listen(('0.0.0.0', 5678))

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(users.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="PEGB",
        version = "1.0",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
