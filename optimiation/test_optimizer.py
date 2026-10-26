# test_optimizer.py

import json

from .optimizer import optimize_sales


# Load test predictions
with open("data/test_predictions.json", "r") as file:
    predictions = json.load(file)


# Test market information
market_data = {
    "Ajmer": {
        "distance_km": 10
    },
    "Jaipur": {
        "distance_km": 130
    }
}


# Farmer information
quantity_kg = 1000


# Temporary MVP assumptions
transport_rate = 15
storage_rate = 0.50


# Run optimizer
result = optimize_sales(
    predictions=predictions,
    quantity_kg=quantity_kg,
    market_data=market_data,
    transport_rate=transport_rate,
    storage_rate=storage_rate
)


# Display recommendation
print("\n================================")
print("     AGRITRADE RECOMMENDATION")
print("================================")

print(
    "Market:",
    result["recommended_market"]
)

print(
    "Date:",
    result["recommended_date"]
)

print(
    "Predicted Price: ₹",
    result["predicted_price"]
)

print(
    "Transport Cost: ₹",
    result["transport_cost"]
)

print(
    "Storage Cost: ₹",
    result["storage_cost"]
)

print(
    "Expected Revenue: ₹",
    result["expected_revenue"]
)

print(
    "Expected Net Profit: ₹",
    result["expected_profit"]
)