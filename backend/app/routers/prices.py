from datetime import date
from backend.app.schemas.market_price import MarketPriceResponse
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.models.market_price import MarketPrice


router = APIRouter(
    prefix="/api/prices",
    tags=["Prices"]
)


@router.get("/", response_model=list[MarketPriceResponse])
def get_prices(
    crop_id: int | None = Query(default=None),
    market_id: int | None = Query(default=None),
    start_date: date | None = Query(default=None),
    end_date: date | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=50, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(MarketPrice)

    if crop_id is not None:
        query = query.filter(MarketPrice.crop_id == crop_id)

    if market_id is not None:
        query = query.filter(MarketPrice.market_id == market_id)

    if start_date is not None:
        query = query.filter(
            MarketPrice.arrival_date >= start_date
        )

    if end_date is not None:
        query = query.filter(
            MarketPrice.arrival_date <= end_date
        )

    prices = query.order_by(
        MarketPrice.arrival_date
    ).offset(skip).limit(limit).all()

    return [MarketPriceResponse.model_validate(price) for price in prices]
