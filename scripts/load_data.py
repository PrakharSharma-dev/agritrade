import os
from pathlib import Path

import pandas as pd
import psycopg2
from dotenv import load_dotenv


# --------------------------------------------------
# Configuration
# --------------------------------------------------

load_dotenv()

CSV_FILE = Path(
    "data/processed/wheat_madanganj_kishangarh.csv"
)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


# --------------------------------------------------
# Load CSV
# --------------------------------------------------

print("Loading processed dataset...")

df = pd.read_csv(CSV_FILE)

df["Arrival_Date"] = pd.to_datetime(
    df["Arrival_Date"]
).dt.date

print(f"Records loaded from CSV: {len(df)}")


# --------------------------------------------------
# Connect to PostgreSQL
# --------------------------------------------------

print("Connecting to PostgreSQL...")

conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()


try:

    # --------------------------------------------------
    # Get Crop ID
    # --------------------------------------------------

    cursor.execute(
        """
        SELECT crop_id
        FROM crops
        WHERE LOWER(crop_name) = LOWER(%s)
        """,
        ("Wheat",)
    )

    crop_result = cursor.fetchone()

    if crop_result is None:
        raise ValueError("Wheat crop was not found.")

    crop_id = crop_result[0]

    print(f"Wheat crop_id: {crop_id}")


    # --------------------------------------------------
    # Get Market ID
    # --------------------------------------------------

    cursor.execute(
        """
        SELECT market_id
        FROM markets
        WHERE market_name = %s
          AND district = %s
          AND state = %s
        """,
        (
            "Madanganj Kishangarh",
            "Ajmer",
            "Rajasthan",
        )
    )

    market_result = cursor.fetchone()

    if market_result is None:
        raise ValueError(
            "Madanganj Kishangarh market was not found."
        )

    market_id = market_result[0]

    print(f"Market ID: {market_id}")


    # --------------------------------------------------
    # Insert market prices
    # --------------------------------------------------

    insert_query = """
        INSERT INTO market_prices (
            market_id,
            crop_id,
            variety,
            grade,
            arrival_date,
            min_price,
            max_price,
            modal_price,
            price_unit
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (
            market_id,
            crop_id,
            variety,
            grade,
            arrival_date
        )
        DO NOTHING
    """

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():

        cursor.execute(
            insert_query,
            (
                market_id,
                crop_id,
                row["Variety"],
                row["Grade"],
                row["Arrival_Date"],
                row["Min_Price"],
                row["Max_Price"],
                row["Modal_Price"],
                "₹/quintal",
            )
        )

        if cursor.rowcount == 1:
            inserted += 1
        else:
            skipped += 1


    # --------------------------------------------------
    # Commit transaction
    # --------------------------------------------------

    conn.commit()

    print("\n========== IMPORT COMPLETE ==========")
    print(f"Records inserted: {inserted}")
    print(f"Records skipped: {skipped}")


except Exception as error:

    conn.rollback()

    print("\nIMPORT FAILED")
    print("Transaction rolled back.")
    print(f"Error: {error}")

    raise


finally:

    cursor.close()
    conn.close()

    print("Database connection closed.")