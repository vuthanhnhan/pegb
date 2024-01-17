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

    async def get_product_with_discount(self, ids: list):
        placeholders = ', '.join(['%s'] * len(ids))
        query = f'SELECT * FROM product as p LEFT JOIN category as c ON p.category_id = c.id WHERE p.id IN ({placeholders})'
        return await self.operation(query, (ids))