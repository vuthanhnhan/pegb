from fastapi import APIRouter, Request
from .type import *
from .repository import UserRepository

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
)

@router.post("/register", status_code=201, responses={
                201: {"model": UsersLoginResponseType, "description": "Register user success"}
                })
async def create(request: Request, data: UsersCreateRequestType):
    result = await UserRepository().create_external_user(data)
    return UsersLoginResponseType(**result.dict())

@router.post("/verify-otp", status_code=201, responses={
                201: {"model": UsersLoginResponseType, "description": "Register user success"}
                })
async def verify_otp(request: Request, data: VerifyOtpRequestType):
    result = await UserRepository().verify_otp(data)
    return UsersLoginResponseType(**result.dict())
