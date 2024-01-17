from fastapi import APIRouter, Request, HTTPException, Response
from .type import *
from .repository import ProductRepository
from .model import ProductModel

router = APIRouter(
    prefix="/api/products",
    tags=["products"],
)

product_model = ProductModel()
@router.post("/", responses={
                201: {"model": ProductCreateResponseType}
                })
async def create(request: Request, data: ProductCreateRequestType):
    result = await product_model.create_product(data)
    return ProductCreateResponseType(**result)


@router.patch("/{_id}", responses={
                200: {"model": ProductUpdateResponseType}
                })
async def edit(request: Request, _id: int, data: ProductUpdateRequestType):
    result = await product_model.update_product(_id, data)
    return ProductUpdateResponseType(**result)

@router.get("/{_id}", responses={
                200: {"model": ProductType, }
            })
async def get(request: Request, _id: str):

    product = await product_model.find_one_by_id(_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return ProductType(**product)

@router.get("/category/{_id}")
async def get_by_category(request: Request, _id: str):

    products = await product_model.find_by({ "category_id": _id })

    return [ProductType(**p) for p in products]


@router.delete("/{_id}", status_code=204)
async def delete(request: Request, _id: int):
    product = await product_model.find_one_by_id(_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await product_model.delete_by_id(_id)

    return Response(status_code=204)