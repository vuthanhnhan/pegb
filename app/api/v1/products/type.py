from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime


class ProductCreateRequestType(BaseModel):
    category_id: int
    name: str
    price: float

class ProductCreateResponseType(BaseModel):
    category_id: int
    name: str
    price: float

class ProductType(BaseModel):
    id: Optional[int]
    category_id: int
    name: str
    price: float

class ProductUpdateType(BaseModel):
    category_id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class ProductUpdateRequestType(BaseModel):
    category_id: Optional[int]
    name: Optional[str]
    price: Optional[float]

class ProductUpdateResponseType(BaseModel):
    category_id: Optional[int]
    name: Optional[str]
    price: Optional[float]
