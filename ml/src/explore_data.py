
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wheat_madanganj_kishangarh.csv"
)


def main():
    df = pd.read_csv(DATA_PATH)

    print("\n1. DATASET SHAPE")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n2. COLUMN NAMES AND DATA TYPES")
    print(df.dtypes.to_string())

    print("\n3. MISSING VALUES")
    print(df.isna().sum().to_string())

    print("\n4. DUPLICATE ROWS")
    print(df.duplicated().sum())

    print("\n5. PRICE SUMMARY")
    for column in ["Min_Price", "Max_Price", "Modal_Price"]:
        if column in df.columns:
            print(f"\n{column}")
            print(df[column].describe())

    print("\n6. DATE RANGE")
    dates = pd.to_datetime(df["Arrival_Date"], errors="coerce")
    print(f"First date: {dates.min()}")
    print(f"Last date:  {dates.max()}")
    print(f"Invalid dates: {dates.isna().sum()}")

    print("\n7. OBSERVATION INTERVALS")
    ordered_dates = dates.dropna().sort_values()
    gaps = ordered_dates.diff().dt.days.dropna()

    print("Days between consecutive observations:")
    print(gaps.describe())
    print("\nMost common intervals:")
    print(gaps.value_counts().head(10).to_string())


if __name__ == "__main__":
    main()
