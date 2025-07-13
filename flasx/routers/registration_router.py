from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..models.models import Travel, ProvinceDiscount
from ..schemas.schemas import TravelCreate, TravelResponse, ProvinceDiscountCreate, ProvinceDiscountResponse
from ..database import get_db
from .auth_router import get_current_user

router = APIRouter()

@router.post("/register_travel", response_model=TravelResponse)
def register_travel(
    travel: TravelCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    db_travel = Travel(
        user_id=current_user.id,
        fullname=travel.fullname,
        destination_province_id=travel.destination_province_id,
        destination_province_name=travel.destination_province_name,
        travel_date=travel.travel_date
    )
    db.add(db_travel)
    db.commit()
    db.refresh(db_travel)
    return db_travel


# Get all registrations
@router.get("/registrations", response_model=list[TravelResponse])
def get_all_registrations(db: Session = Depends(get_db)):
    return db.query(Travel).all()

# Province Discount APIs
@router.post("/province_discount", response_model=ProvinceDiscountResponse)
def create_province_discount(
    discount: ProvinceDiscountCreate,
    db: Session = Depends(get_db)
):
    db_discount = ProvinceDiscount(
        province=discount.province,
        discount_percentage=discount.discount_percentage,
        secondary_province=discount.secondary_province
    )
    db.add(db_discount)
    db.commit()
    db.refresh(db_discount)
    return db_discount

@router.get("/province_discounts", response_model=list[ProvinceDiscountResponse])
def get_province_discounts(db: Session = Depends(get_db)):
    return db.query(ProvinceDiscount).all()
