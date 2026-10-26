
from pathlib import Path

import joblib
import pandas as pd


# Find project files
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wheat_madanganj_kishangarh.csv"
)

MODEL_PATH = (
    PROJECT_ROOT
    / "ml"
    / "models"
    / "wheat_price_model.joblib"
)


def main():
    # Check required files exist
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Saved model not found: {MODEL_PATH}. "
            "Run ml/src/train_model.py first."
        )

    # Load the dataset
    df = pd.read_csv(DATA_PATH)

    df["Arrival_Date"] = pd.to_datetime(
        df["Arrival_Date"], errors="coerce", dayfirst=True
    )
    df["Modal_Price"] = pd.to_numeric(
        df["Modal_Price"], errors="coerce"
    )

    df = (
        df.dropna(subset=["Arrival_Date", "Modal_Price"])
        .sort_values("Arrival_Date")
        .reset_index(drop=True)
    )

    if len(df) < 3:
        raise ValueError("At least three valid price observations are required.")

    # Extract the latest three observed prices
    recent_prices = df["Modal_Price"].tail(3).tolist()

    # Features must be ordered newest to oldest:
    # lag_1 = latest price, lag_2 = previous price, lag_3 = third previous
    features = pd.DataFrame(
        [[recent_prices[2], recent_prices[1], recent_prices[0]]],
        columns=["lag_1", "lag_2", "lag_3"],
    )

    # Load the trained model artifact
    saved = joblib.load(MODEL_PATH)
    model = saved["model"]

    expected_features = saved["features"]
    features = features[expected_features]

    # Predict the next recorded price
    prediction = float(model.predict(features)[0])

    print("\nAGRI TRADE — WHEAT PRICE PREDICTION")
    print("=" * 42)
    print("Latest recorded observations:")

    for _, row in df.tail(3).iterrows():
        print(
            f"  {row['Arrival_Date'].date()}: "
            f"₹{row['Modal_Price']:.2f} per quintal"
        )

    print(f"\nPredicted next recorded price: ₹{prediction:.2f} per quintal")
    print("\nNote: This is a model prediction, not a guaranteed market price.")


if __name__ == "__main__":
    main()
