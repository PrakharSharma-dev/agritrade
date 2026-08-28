from sqlalchemy import (
    Column,
    BigInteger,
    Integer,
    String,
    Numeric,
    Date,
    DateTime,
    ForeignKey,
)

from backend.app.database import Base


class MarketPrice(Base):
    __tablename__ = "market_prices"

    price_id = Column(BigInteger, primary_key=True, nullable=False)

    market_id = Column(
        Integer,
        ForeignKey("markets.market_id"),
        nullable=False,
    )

    crop_id = Column(
        Integer,
        ForeignKey("crops.crop_id"),
        nullable=False,
    )

    variety = Column(String, nullable=True)
    grade = Column(String, nullable=True)

    arrival_date = Column(Date, nullable=False)

    min_price = Column(Numeric, nullable=True)
    max_price = Column(Numeric, nullable=True)
    modal_price = Column(Numeric, nullable=True)

    price_unit = Column(String, nullable=True)

    created_at = Column(DateTime, nullable=True)