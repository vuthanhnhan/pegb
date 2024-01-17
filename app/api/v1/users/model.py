from app.utils.database import Database
from .type import UserType

class UserModel(Database):
    def __init__(self) -> None:
        super().__init__('user')

    async def insert_user(self, user_data: UserType):
        query = "INSERT INTO user (email, password, name, user_type, otp, expire_otp) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (user_data.email, user_data.password, user_data.name, user_data.user_type, user_data.otp, user_data.expire_otp)
        return await self.operation(query, values)
    
    async def get_user_by_email(self, email):
        query = "SELECT * FROM user WHERE email = %s"
        values = (email,)

        result = await self.operation(query, values)
        if len(result): return UserType(**result[0])
        return None  
