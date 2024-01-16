from app.utils.database import Database
from .type import * 

class ProductModel(Database):
    def __init__(self) -> None:
        super().__init__('product')

    async def create_product(self, product: ProductType):
        await self.create(product.dict(exclude_none=True))
        return await self.find_one_by(product.dict(exclude_none=True))
        

    async def update_product(self, id, product: ProductUpdateType):
        await self.update_by_id(id, product.dict(exclude_none=True))
        return await self.find_one_by(product.dict(exclude_none=True))
