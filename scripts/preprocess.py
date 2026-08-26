import pandas as pd
from pathlib import Path


# ============================================================
# Configuration
# ============================================================

INPUT_FILE = Path("data/raw/wheat_daily_prices.csv")

OUTPUT_DIR = Path("data/processed")
OUTPUT_FILE = OUTPUT_DIR / "wheat_madanganj_kishangarh.csv"

TARGET_MARKET = "Madanganj Kishangarh"


# ============================================================
# 1. Load raw dataset
# ============================================================

print("Loading raw dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Raw records: {len(df)}")


# ============================================================
# 2. Convert date
# ============================================================

df["Arrival_Date"] = pd.to_datetime(
    df["Arrival_Date"],
    dayfirst=True,
    errors="coerce"
)


# ============================================================
# 3. Filter selected market
# ============================================================

df = df[
    df["Market"].str.strip() == TARGET_MARKET
].copy()

print(f"Records for {TARGET_MARKET}: {len(df)}")


# ============================================================
# 4. Validate important fields
# ============================================================

required_columns = [
    "Arrival_Date",
    "Market",
    "Commodity",
    "Variety",
    "Grade",
    "Min_Price",
    "Max_Price",
    "Modal_Price"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )


# Remove rows with invalid dates
df = df.dropna(
    subset=["Arrival_Date"]
)


# Remove rows with missing prices
df = df.dropna(
    subset=[
        "Min_Price",
        "Max_Price",
        "Modal_Price"
    ]
)


# Remove invalid prices
df = df[
    (df["Min_Price"] >= 0) &
    (df["Max_Price"] >= 0) &
    (df["Modal_Price"] >= 0)
].copy()


# ============================================================
# 5. Check price consistency
# ============================================================

invalid_price_rows = df[
    (df["Max_Price"] < df["Min_Price"]) |
    (df["Modal_Price"] < df["Min_Price"]) |
    (df["Modal_Price"] > df["Max_Price"])
]

if len(invalid_price_rows) > 0:
    print(
        f"Removing {len(invalid_price_rows)} "
        "invalid price records."
    )

    df = df.drop(
        invalid_price_rows.index
    )


# ============================================================
# 6. Aggregate multiple observations on same date
# ============================================================

print("\nChecking multiple observations per date...")

duplicate_dates = (
    df.groupby("Arrival_Date")
    .size()
)

duplicate_dates = duplicate_dates[
    duplicate_dates > 1
]

print(
    f"Dates with multiple observations: "
    f"{len(duplicate_dates)}"
)


# For the forecasting dataset we need one value per date.
#
# Modal_Price:
#     arithmetic mean of multiple observations
#
# Min_Price:
#     minimum observed price
#
# Max_Price:
#     maximum observed price

clean_df = (
    df.groupby(
        [
            "Arrival_Date",
            "Market",
            "Commodity",
            "Variety",
            "Grade"
        ],
        as_index=False
    )
    .agg(
        Min_Price=("Min_Price", "min"),
        Max_Price=("Max_Price", "max"),
        Modal_Price=("Modal_Price", "mean"),
        Commodity_Code=("Commodity_Code", "first"),
        District=("District", "first"),
        State=("State", "first")
    )
)


# ============================================================
# 7. Sort chronologically
# ============================================================

clean_df = clean_df.sort_values(
    "Arrival_Date"
).reset_index(drop=True)


# ============================================================
# 8. Round aggregated prices
# ============================================================

clean_df["Min_Price"] = clean_df[
    "Min_Price"
].round(2)

clean_df["Max_Price"] = clean_df[
    "Max_Price"
].round(2)

clean_df["Modal_Price"] = clean_df[
    "Modal_Price"
].round(2)


# ============================================================
# 9. Final validation
# ============================================================

print("\n========== FINAL VALIDATION ==========")

print(
    f"Processed records: {len(clean_df)}"
)

print(
    f"Unique dates: "
    f"{clean_df['Arrival_Date'].nunique()}"
)

print(
    f"Start date: "
    f"{clean_df['Arrival_Date'].min().date()}"
)

print(
    f"End date: "
    f"{clean_df['Arrival_Date'].max().date()}"
)

print(
    f"Missing values:\n"
    f"{clean_df.isnull().sum()}"
)

print(
    f"Duplicate dates after processing: "
    f"{clean_df['Arrival_Date'].duplicated().sum()}"
)


# ============================================================
# 10. Save processed dataset
# ============================================================

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

clean_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n========== PREPROCESSING COMPLETE ==========")

print(
    f"Saved processed dataset to:\n"
    f"{OUTPUT_FILE}"
)