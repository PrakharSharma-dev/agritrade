from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.schemas.crop import CropResponse
from backend.app.database import get_db
from backend.app.models.crop import Crop


router = APIRouter(
    prefix="/api/crops",
    tags=["Crops"]
)


@router.get("/", response_model=list[CropResponse])
def get_crops(db: Session = Depends(get_db)):
    crops = db.query(Crop).all()

    return [CropResponse.model_validate(crop) for crop in crops]    