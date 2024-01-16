from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime

class UsersCreateRequestType(BaseModel):
    email: EmailStr
    password: str

class VerifyOtpRequestType(BaseModel):
    email: EmailStr
    otp: str

class UsersLoginResponseType(BaseModel):
    email: EmailStr

class UserType(BaseModel):
    email: EmailStr
    password: str
    user_type: Optional[Literal['internal', 'external']] = 'external',
    otp: Optional[str]
    expire_otp: Optional[datetime]
    is_verified: Optional[bool] = False