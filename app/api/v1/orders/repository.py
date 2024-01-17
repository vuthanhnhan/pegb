from .type import *
from .model import OrderModel
from app.api.v1.products.model import ProductModel
from app.api.v1.tiers.model import TierModel

class OrderRepository:
    __order_model = OrderModel()
    __product_model = ProductModel()
    __tier_model = TierModel()

    async def make_order(self, product_ids: list, user_id):
        total_price = 0
        product_price_detail = []
        product_detail = await self.__product_model.get_product_with_discount(product_ids)
        for product in product_detail:
            # price is not None, discount can None
            discount = product['price'] * product.get('discount', 0) / 100
            original_price = product['price']
            discount_price = original_price - discount
            total_price += discount_price
            product_price_detail.append({ 'original_price': round(original_price, 2), 
                                         'discount_price': round(discount_price, 2),
                                          'product_name': product['name']
                                           })

        # handle register for User
        user_histroy = await self.__order_model.get_order_history(user_id, 'complete')

        user_tier = await self.__tier_model.find_tier_by_complete_order(len(user_histroy))

        user_discount_price = total_price - total_price * user_tier.get('discount', 0) / 100
        user_discount_price = round(user_discount_price, 2)
        total_price = round(total_price, 2)

        await self.__order_model.save_order(OrderType(**{ "total_amount": user_discount_price, "user_id": user_id }))
        return { 
            "user_discount_price": user_discount_price,
            "product_discount_price": total_price,
            "product_price_detail": product_price_detail,
            "user_rank": user_tier['category_name']
        }