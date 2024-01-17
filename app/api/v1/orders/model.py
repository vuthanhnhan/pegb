from app.utils.database import Database
from .type import *

class OrderModel(Database):
    def __init__(self) -> None:
        super().__init__('cart_order')

    async def get_order_history(self, user_id: int, status: str = None):
        query = { 'user_id': user_id }
        if status is not None:
            query['status'] = status
        return await self.find_by(query)

    async def save_order(self, data: OrderType):
        query = """
            INSERT INTO cart_order (user_id, status, total_amount)
            VALUES (%s, %s, %s)
        """
        values = (data.user_id, data.status, data.total_amount)

        await self.operation(query, values)
