from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.schemas.market import MarketResponse
from backend.app.database import get_db
from backend.app.models.market import Market


router = APIRouter(
    prefix="/api/markets",
    tags=["Markets"]
)


@router.get("/", response_model=list[MarketResponse])
def get_markets(db: Session = Depends(get_db)):
    markets = db.query(Market).all()

    return [MarketResponse.model_validate(market) for market in markets]