from fastapi import APIRouter, Request
from app.utils.auth import require_permission
from .type import *
from .repository import OrderRepository
from .model import OrderModel

router = APIRouter(
    prefix="/api/orders",
    tags=["orders"],
)

order_model = OrderModel()
@router.post("/make", responses={
                200: {"model": MakeOrdersResponseType}
            })
@require_permission
async def make_order(request: Request, data: MakeOrderRequestType):
    result = await OrderRepository().make_order(data.product_ids, request.state.payload['id'])
    return MakeOrdersResponseType(**result)

@router.get("/history",responses={
                200: {"model": OrderHistoryResponse}
            })
@require_permission
async def get_history(request: Request):
    result = await order_model.get_order_history(request.state.payload['id'])
    return [OrderHistoryResponse(**r) for r in result]