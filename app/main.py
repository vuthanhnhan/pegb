from fastapi import FastAPI, Response, Request
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

import app.api.v1.users.router as users
import app.api.v1.products.router as products
import app.api.v1.categories.router as categories
import app.api.v1.orders.router as orders

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import debugpy
debugpy.listen(('0.0.0.0', 5678))

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(users.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(orders.router)

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
