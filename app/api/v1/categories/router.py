from fastapi import APIRouter, Request, HTTPException, Response
from .type import *
from .model import CategoryModel

router = APIRouter(
    prefix="/api/categories",
    tags=["categories"],
)

category_model = CategoryModel()
@router.get("/", responses={
                200: {"model": CategoryType }
            })
async def get_all(request: Request):
    result = await category_model.find_all()
    return [CategoryType(**r) for r in result]