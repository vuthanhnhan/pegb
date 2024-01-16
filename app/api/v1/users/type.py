from pydantic import BaseModel

class ModelUsersClientsCreateRequest(BaseModel):
    email: str
    password: str

class ModelUsersClientsLoginResponse(BaseModel):
    access_token: str