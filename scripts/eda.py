import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

FILE_PATH = "data/raw/wheat_daily_prices.csv"

df = pd.read_csv(FILE_PATH)

# Convert date
df["Arrival_Date"] = pd.to_datetime(
    df["Arrival_Date"],
    dayfirst=True,
    errors="coerce"
)

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMNS ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== FIRST 5 RECORDS ==========")
print(df.head())


# --------------------------------------------------
# 2. Missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# --------------------------------------------------
# 3. Duplicate analysis
# --------------------------------------------------

print("\n========== EXACT DUPLICATES ==========")
print(df.duplicated().sum())

duplicate_key = [
    "Arrival_Date",
    "Market",
    "Commodity",
    "Variety",
    "Grade"
]

print("\n========== DUPLICATE DATE/MARKET RECORDS ==========")
print(
    df.duplicated(
        subset=duplicate_key,
        keep=False
    ).sum()
)


# --------------------------------------------------
# 4. Basic price statistics
# --------------------------------------------------

print("\n========== PRICE STATISTICS ==========")

print(
    df[
        ["Min_Price", "Max_Price", "Modal_Price"]
    ].describe()
)


# --------------------------------------------------
# 5. Unique values
# --------------------------------------------------

print("\n========== UNIQUE MARKETS ==========")
print(df["Market"].value_counts())

print("\n========== GRADES ==========")
print(df["Grade"].value_counts())

print("\n========== VARIETIES ==========")
print(df["Variety"].value_counts())


# --------------------------------------------------
# 6. Date range
# --------------------------------------------------

print("\n========== DATE RANGE ==========")

print("Start:", df["Arrival_Date"].min())
print("End  :", df["Arrival_Date"].max())


# --------------------------------------------------
# 7. Average modal price by market
# --------------------------------------------------

market_summary = (
    df.groupby("Market")["Modal_Price"]
    .agg(
        records="count",
        mean="mean",
        median="median",
        minimum="min",
        maximum="max",
        std="std"
    )
    .sort_values("mean", ascending=False)
)

print("\n========== MARKET PRICE SUMMARY ==========")
print(market_summary)


# --------------------------------------------------
# 8. Plot average price by market
# --------------------------------------------------

market_summary["mean"].sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Average Modal Price by Market")
plt.xlabel("Average Modal Price")
plt.ylabel("Market")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 9. Overall price distribution
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.hist(
    df["Modal_Price"],
    bins=30
)

plt.title("Distribution of Modal Prices")
plt.xlabel("Modal Price")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 10. Price over time
# --------------------------------------------------

plt.figure(figsize=(12, 6))

plt.scatter(
    df["Arrival_Date"],
    df["Modal_Price"],
    s=10
)

plt.title("Wheat Modal Price Over Time")
plt.xlabel("Arrival Date")
plt.ylabel("Modal Price")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 11. Monthly average price
# --------------------------------------------------

monthly = (
    df.set_index("Arrival_Date")
    .resample("ME")["Modal_Price"]
    .mean()
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly.index,
    monthly.values
)

plt.title("Monthly Average Wheat Modal Price")
plt.xlabel("Date")
plt.ylabel("Average Modal Price")

plt.tight_layout()
plt.show()
# --------------------------------------------------
# 12. Market-wise price trends
# --------------------------------------------------

plt.figure(figsize=(14, 7))

for market, market_data in df.groupby("Market"):
    market_data = market_data.sort_values("Arrival_Date")

    plt.plot(
        market_data["Arrival_Date"],
        market_data["Modal_Price"],
        label=market
    )

plt.title("Wheat Modal Price Trend by Market")
plt.xlabel("Arrival Date")
plt.ylabel("Modal Price")
plt.legend()
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 13. Monthly observation count
# --------------------------------------------------

monthly_records = (
    df.set_index("Arrival_Date")
    .resample("ME")
    .size()
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_records.index,
    monthly_records.values
)

plt.title("Number of Wheat Price Records per Month")
plt.xlabel("Month")
plt.ylabel("Number of Records")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 14. Average price by month of year
# --------------------------------------------------

df["Month"] = df["Arrival_Date"].dt.month

monthly_seasonality = (
    df.groupby("Month")["Modal_Price"]
    .mean()
)

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_seasonality.index,
    monthly_seasonality.values,
    marker="o"
)

plt.title("Average Wheat Modal Price by Month")
plt.xlabel("Month")
plt.ylabel("Average Modal Price")
plt.xticks(range(1, 13))

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 15. Average price by year
# --------------------------------------------------

df["Year"] = df["Arrival_Date"].dt.year

yearly_average = (
    df.groupby("Year")["Modal_Price"]
    .mean()
)

print("\n========== YEARLY AVERAGE MODAL PRICE ==========")
print(yearly_average)


# --------------------------------------------------
# 16. Price volatility by market
# --------------------------------------------------

market_volatility = (
    df.groupby("Market")["Modal_Price"]
    .agg(
        mean="mean",
        std="std",
        minimum="min",
        maximum="max"
    )
    .sort_values("std", ascending=False)
)

print("\n========== PRICE VOLATILITY BY MARKET ==========")
print(market_volatility)


# --------------------------------------------------
# 17. Rolling average for strongest market
# --------------------------------------------------

# Madanganj Kishangarh has the strongest historical coverage
main_market = "Madanganj Kishangarh"

market_df = (
    df[df["Market"] == main_market]
    .sort_values("Arrival_Date")
    .copy()
)

market_df["Rolling_30_Day_Average"] = (
    market_df["Modal_Price"]
    .rolling(window=30, min_periods=1)
    .mean()
)

plt.figure(figsize=(14, 6))

plt.plot(
    market_df["Arrival_Date"],
    market_df["Modal_Price"],
    alpha=0.4,
    label="Daily Modal Price"
)

plt.plot(
    market_df["Arrival_Date"],
    market_df["Rolling_30_Day_Average"],
    label="30-Day Rolling Average"
)

plt.title(
    "Wheat Price — Madanganj Kishangarh"
)
plt.xlabel("Arrival Date")
plt.ylabel("Modal Price")
plt.legend()

plt.tight_layout()
plt.show()
print("\n========== EDA COMPLETE ==========") 