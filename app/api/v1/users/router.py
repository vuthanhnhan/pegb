from fastapi import APIRouter, Request, Query, Depends
from .type import *
from .repository import UserRepository

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/register", status_code=201, responses={
                201: {"model": UsersClientsLoginResponseType, "description": "Register user success"}
                })
async def create(request: Request, data: UsersClientsCreateRequestType):
    result = await UserRepository().create_external_user(data)
    return UsersClientsLoginResponseType(**result.dict())

@router.post("/verify-otp", status_code=201, responses={
                201: {"model": UsersClientsLoginResponseType, "description": "Register user success"}
                })
async def verify_otp(request: Request, data: VerifyOtpRequestType):
    result = await UserRepository().verify_otp(data)
    return UsersClientsLoginResponseType(**result.dict())
