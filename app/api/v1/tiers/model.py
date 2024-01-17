from app.utils.database import Database

class TierModel(Database):
    def __init__(self) -> None:
        super().__init__('tier')

    async def find_tier_by_complete_order(self, total_order):
        query = 'SELECT * FROM tier WHERE %s BETWEEN min_orders AND COALESCE(max_orders, %s)'
        values = (total_order, total_order)
        result = await self.operation(query, values)
        return result[0]


