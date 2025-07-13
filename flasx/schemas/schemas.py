from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TravelCreate(BaseModel):
    user_id: int
    fullname: str
    destination_province_id: int  # ProvinceDiscount id
    destination_province_name: str
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

class ProvinceDiscountCreate(BaseModel):
    province: str
    discount_percentage: int
    secondary_province: int

class ProvinceDiscountResponse(ProvinceDiscountCreate):
    id: int

    class Config:
        from_attributes = True