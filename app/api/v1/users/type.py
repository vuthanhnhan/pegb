from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime

class UsersCreateRequestType(BaseModel):
    email: EmailStr
    password: str

class VerifyOtpRequestType(BaseModel):
    email: EmailStr
    otp: str

class UsersCreateResponseType(BaseModel):
    email: EmailStr

class UserType(BaseModel):
    id: Optional[int]
    email: EmailStr
    password: str
    user_type: Optional[Literal['internal', 'external']] = 'external',
    otp: Optional[str]
    expire_otp: Optional[datetime]
    is_verified: Optional[bool] = False

class UserLoginRequestType(BaseModel):
    email: EmailStr
    password: str

class UserLoginResponseType(BaseModel):
    access_token: str