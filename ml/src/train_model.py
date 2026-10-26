
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wheat_madanganj_kishangarh.csv"
)

MODEL_DIR = PROJECT_ROOT / "ml" / "models"
MODEL_PATH = MODEL_DIR / "wheat_price_model.joblib"

TARGET = "Modal_Price"
LAG_FEATURES = ["lag_1", "lag_2", "lag_3"]


def main():
    # 1. Load the processed dataset
    df = pd.read_csv(DATA_PATH)

    required_columns = ["Arrival_Date", TARGET]
    missing = set(required_columns) - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    # 2. Clean and sort observations chronologically
    df["Arrival_Date"] = pd.to_datetime(
    df["Arrival_Date"], errors="coerce"
      )
    df[TARGET] = pd.to_numeric(df[TARGET], errors="coerce")

    df = df.dropna(subset=["Arrival_Date", TARGET])
    df = df.sort_values("Arrival_Date").reset_index(drop=True)

    # 3. Create features from previous observed prices
    for lag in range(1, 4):
        df[f"lag_{lag}"] = df[TARGET].shift(lag)

    # Each row predicts its price using only earlier observations
    df = df.dropna(subset=LAG_FEATURES + [TARGET]).reset_index(drop=True)

    X = df[LAG_FEATURES]
    y = df[TARGET]

    # 4. Split chronologically: earlier data for training,
    #    later data for testing
    split_index = int(len(df) * 0.8)

    X_train = X.iloc[:split_index]
    X_test = X.iloc[split_index:]
    y_train = y.iloc[:split_index]
    y_test = y.iloc[split_index:]

    if len(X_train) == 0 or len(X_test) == 0:
        raise ValueError("Not enough observations for train/test evaluation.")

    # 5. Baseline: predict the next price using the latest
    #    previously observed price
    baseline_predictions = X_test["lag_1"]

    # 6. Train the machine-learning model
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        min_samples_leaf=2,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # 7. Evaluate both approaches on the same test observations
    results = {
        "Baseline (previous price)": baseline_predictions,
        "Random Forest": predictions,
    }

    print("\nWHEAT PRICE FORECASTING RESULTS")
    print("=" * 45)
    print(f"Usable observations: {len(df)}")
    print(f"Training observations: {len(X_train)}")
    print(f"Testing observations: {len(X_test)}")
    print(
    f"Test period: {df['Arrival_Date'].iloc[split_index].date()}"
    f" to {df['Arrival_Date'].iloc[-1].date()}"
     ) 
    for name, predicted in results.items():
        mae = mean_absolute_error(y_test, predicted)
        rmse = mean_squared_error(y_test, predicted) ** 0.5

        print(f"\n{name}")
        print(f"  MAE:  ₹{mae:.2f} per quintal")
        print(f"  RMSE: ₹{rmse:.2f} per quintal")

    # 8. Save the trained model and its feature names
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        {
            "model": model,
            "features": LAG_FEATURES,
            "target": TARGET,
        },
        MODEL_PATH,
    )

    print(f"\nSaved model to: {MODEL_PATH}")


if __name__ == "__main__":
    main()
