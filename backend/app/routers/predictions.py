
from pathlib import Path

import joblib
import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.models.market_price import MarketPrice


router = APIRouter(
    prefix="/api/predictions",
    tags=["Predictions"],
)

PROJECT_ROOT = Path(__file__).resolve().parents[3]
MODEL_PATH = (
    PROJECT_ROOT
    / "ml"
    / "models"
    / "wheat_price_model.joblib"
)


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Trained model not found: {MODEL_PATH}"
        )

    saved = joblib.load(MODEL_PATH)

    return saved["model"], saved["features"]


@router.get("/")
def predict_price(
    crop_id: int = Query(..., description="Crop ID"),
    market_id: int = Query(..., description="Market ID"),
    db: Session = Depends(get_db),
):
    # Get the latest recorded prices for this crop and market.
    rows = (
        db.query(MarketPrice)
        .filter(
            MarketPrice.crop_id == crop_id,
            MarketPrice.market_id == market_id,
            MarketPrice.modal_price.isnot(None),
        )
        .order_by(
            MarketPrice.arrival_date.desc(),
            MarketPrice.price_id.desc(),
        )
        .limit(3)
        .all()
    )

    if len(rows) < 3:
        raise HTTPException(
            status_code=400,
            detail=(
                "At least three recorded modal prices are required "
                "for this crop and market."
            ),
        )

    # The query returns newest to oldest.
    # The model expects lag_1, lag_2, lag_3 in that order.
    recent_prices = [float(row.modal_price) for row in rows]

    features = pd.DataFrame(
        [[recent_prices[0], recent_prices[1], recent_prices[2]]],
        columns=["lag_1", "lag_2", "lag_3"],
    )

    try:
        model, feature_names = load_model()
        features = features[feature_names]
        prediction = float(model.predict(features)[0])
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {exc}",
        )

    return {
        "crop_id": crop_id,
        "market_id": market_id,
        "latest_observation_date": rows[0].arrival_date.isoformat(),
        "latest_modal_price": recent_prices[0],
        "predicted_price": round(prediction, 2),
        "price_unit": rows[0].price_unit or "INR per quintal",
        "forecast_type": "next recorded observation",
        "model": "Random Forest",
        "note": (
            "This is an experimental forecast, not a guaranteed price. "
            "The model has not outperformed the previous-price baseline "
            "in the current evaluation."
        ),
    }
