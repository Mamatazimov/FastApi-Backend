from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    message: str
    gender: str
    

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
