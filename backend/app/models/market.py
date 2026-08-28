from sqlalchemy import Column, Integer, String, Numeric, DateTime
from backend.app.database import Base


class Market(Base):
    __tablename__ = "markets"

    market_id = Column(Integer, primary_key=True, nullable=False)
    market_name = Column(String, nullable=False)
    district = Column(String, nullable=True)
    state = Column(String, nullable=False)
    latitude = Column(Numeric, nullable=True)
    longitude = Column(Numeric, nullable=True)
    created_at = Column(DateTime, nullable=True)