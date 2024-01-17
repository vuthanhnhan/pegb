from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime

class MakeOrderRequestType(BaseModel):
    product_ids: list[int]

class ProductPriceDetail(BaseModel):
    product_name: str
    original_price: float
    discount_price: float

class MakeOrdersResponseType(BaseModel):
    user_discount_price: float
    product_discount_price: float
    product_price_detail: list[ProductPriceDetail]
    user_rank: str

class OrderType(BaseModel):
    user_id: int
    status: Literal['pending', 'complete'] = 'pending'
    total_amount: float