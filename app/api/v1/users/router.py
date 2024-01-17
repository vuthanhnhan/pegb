from fastapi import APIRouter, Request
from .type import *
from .repository import UserRepository
from app.utils.auth import require_permission

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
)

@router.post("/register", status_code=201, responses={
                201: {"model": UsersCreateResponseType, "description": "Register user success"}
                })
async def create(request: Request, data: UsersCreateRequestType):
    result = await UserRepository().create_external_user(data)
    return UsersCreateResponseType(**result.dict())

@router.post("/login", status_code=201, responses={ 201: {"model": UserLoginResponseType} })
async def create(request: Request, data: UserLoginRequestType):
    result = await UserRepository().login(data)
    return UserLoginResponseType(**result)

@router.get("/me", responses={
                200: {"model": UserMeResponseType}
            })
@require_permission
async def get_me(request: Request):
   
    item = await UserRepository().get_me(request)
    return UserMeResponseType(**item)

@router.post("/verify-otp", status_code=201, responses={
                201: {"model": UsersCreateResponseType, "description": "Register user success"}
                })
async def verify_otp(request: Request, data: VerifyOtpRequestType):
    result = await UserRepository().verify_otp(data)
    return UsersCreateResponseType(**result.dict())
