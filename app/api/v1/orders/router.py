from fastapi import APIRouter, Request
from app.utils.auth import require_permission
from .type import *
from .repository import OrderRepository

router = APIRouter(
    prefix="/api/orders",
    tags=["orders"],
)

@router.post("/make", responses={
                200: {"model": MakeOrdersResponseType}
            })
@require_permission
async def make_order(request: Request, data: MakeOrderRequestType):
    result = await OrderRepository().make_order(data.product_ids, request.state.payload['id'])
    return MakeOrdersResponseType(**result)