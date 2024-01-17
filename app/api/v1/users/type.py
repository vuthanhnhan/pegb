from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime

class UsersCreateRequestType(BaseModel):
    email: EmailStr
    name: str
    password: str

class VerifyOtpRequestType(BaseModel):
    email: EmailStr
    otp: str

class UsersCreateResponseType(BaseModel):
    email: EmailStr
    name: str

class UserType(BaseModel):
    id: Optional[int]
    email: EmailStr
    name: str
    password: str
    user_type: Optional[Literal['internal', 'external']] = 'external',
    otp: Optional[str]
    expire_otp: Optional[datetime]
    is_verified: Optional[bool] = False

class UserMeResponseType(BaseModel):
    id: int
    name: str
    email: EmailStr
    user_type: Optional[Literal['internal', 'external']]

class UserLoginRequestType(BaseModel):
    email: EmailStr
    password: str

class UserLoginResponseType(BaseModel):
    access_token: str