from datetime import datetime

from pydantic import BaseModel


class CropResponse(BaseModel):
    crop_id: int
    crop_name: str
    created_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }