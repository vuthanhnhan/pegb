from .type import *
from .model import ProductModel
from app.api.v1.users.model import UserModel
from fastapi import HTTPException

class ProductRepository:
    __product_model = ProductModel()
    __user_model = UserModel()

    async def check_user_same_department(self, product_id, user_id):
        department_id = await self.__product_model.get_department_product(product_id)
        if not await self.__user_model.is_same_department(user_id, department_id):
            raise HTTPException(status_code=403, detail="Not permission")
        

