from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TravelCreate(BaseModel):
    user_id: int
    fullname: str
    destination_province: str
    travel_date: datetime

class TravelResponse(TravelCreate):
    id: int

    class Config:
        from_attributes = True

class UserRegister(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    phone: Optional[str] = None
    email: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str
