from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class MarketResponse(BaseModel):
    market_id: int
    market_name: str
    district: str | None = None
    state: str
    latitude: Decimal | None = None
    longitude: Decimal | None = None
    created_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }