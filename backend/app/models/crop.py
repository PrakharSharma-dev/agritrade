from sqlalchemy import Column, Integer, String, DateTime
from backend.app.database import Base


class Crop(Base):
    __tablename__ = "crops"

    crop_id = Column(Integer, primary_key=True, nullable=False)
    crop_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=True)