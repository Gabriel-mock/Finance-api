from pydantic import BaseModel, Field

class UserRegisterRequest(BaseModel):
    email: str
    password: str = Field(..., min_length=6)

class UserLoginRequest(BaseModel):
    email: str
    password: str