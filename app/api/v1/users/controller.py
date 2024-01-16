from fastapi import APIRouter, Request, Query, Depends
from .type import *
from app.utils.database import Database

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/register", status_code=201, responses={
                201: {"model": ModelUsersClientsLoginResponse, "description": "Register user success"}
                })
async def create(request: Request, data: ModelUsersClientsCreateRequest):
    result = await Database().operation('SELECT * from users')
    return result
    