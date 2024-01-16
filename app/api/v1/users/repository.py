import bcrypt
from .type import *
from .model import UserModel
import secrets, string
import datetime
from fastapi import HTTPException
from .const import SECRET_KEY
from jose import jwt

class UserRepository:
    __user_model = UserModel()
    
    async def login(self, data: UserLoginRequestType):
        user = await self.__user_model.get_user_by_email(data.email)
        if not user:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        
        if not self.verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        
        return {
            "access_token": self.create_access_token({ "id": user.id })
        }
        
    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        expire = int(expire.timestamp())
        to_encode.update({"expire": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
        return encoded_jwt

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return f"{hashed_password.decode('utf-8')}:{salt.decode('utf-8')}"

    def verify_password(self, input_password: str, stored_password: str) -> bool:
        hashed_password, salt = stored_password.split(':')
        input_password_hashed = bcrypt.hashpw(input_password.encode('utf-8'), salt.encode('utf-8'))
        return hashed_password == input_password_hashed.decode('utf-8')

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
