from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel


class MarketPriceResponse(BaseModel):
    price_id: int
    market_id: int
    crop_id: int
    variety: str | None = None
    grade: str | None = None
    arrival_date: date
    min_price: Decimal | None = None
    max_price: Decimal | None = None
    modal_price: Decimal | None = None
    price_unit: str | None = None
    created_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }