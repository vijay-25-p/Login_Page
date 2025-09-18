from pydantic import BaseModel, EmailStr, constr


class UserCreate(BaseModel):
    name: constr(min_length=2)
    email: EmailStr
    password: constr(min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str
