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
    
    async def get_department_product(self, product_id):
        # Category id can not null so use inner join
        query = 'SELECT department_id from category as c INNER JOIN product as p on c.id = p.category_id WHERE p.id = %s'
        results = await self.operation(query, (product_id))
        if not len(results): return False
        return results[0]['department_id']

        