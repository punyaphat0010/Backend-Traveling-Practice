from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..models.models import Travel
from ..schemas.schemas import TravelCreate, TravelResponse
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
        destination_province=travel.destination_province,
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
