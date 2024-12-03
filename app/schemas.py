from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    user_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

class UserLogin(BaseModel):
    email: EmailStr
    password: str


    class Config:
        orm_mode = True
