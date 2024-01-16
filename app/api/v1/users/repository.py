import bcrypt
from .type import UserType, VerifyOtpRequestType
from .model import UserModel
import secrets, string
import datetime
from fastapi import HTTPException

class UserRepository:
    __user_model = UserModel()
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def generate_otp(self, length=6):
        otp = ''.join(secrets.choice(string.digits) for _ in range(length))
        return otp

    async def create_external_user(self, user: UserType):
        hashed_password = self.hash_password(user.password)
        user.password = hashed_password
        user = UserType(**user.dict(exclude_none=True))
        user.otp = self.generate_otp()
        user.expire_otp = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        await self.__user_model.insert_user(user)

        return await self.__user_model.get_user_by_email(user.email)
    
    async def verify_otp(self, data: VerifyOtpRequestType):
        user = await self.__user_model.get_user_by_email(data.email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        current_time = datetime.datetime.utcnow()
        if current_time > user.expire_otp or data.otp != user.otp:
            raise HTTPException(status_code=400, detail="Invalid OTP")

        user.is_verified = True
        await self.__user_model.update({ "email": data.email }, { "is_verified": True })
        return await self.__user_model.get_user_by_email(user.email)
