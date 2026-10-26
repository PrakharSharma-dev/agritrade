# optimizer.py

from .costs import (
    calculate_revenue,
    calculate_transport_cost,
    calculate_storage_cost,
    calculate_net_profit
)


def optimize_sales(
    predictions,
    quantity_kg,
    market_data,
    transport_rate,
    storage_rate
):

    results = []

    for prediction in predictions:

        market = prediction["market"]
        date = prediction["date"]
        price = prediction["predicted_price"]
        storage_days = prediction["storage_days"]

        distance = market_data[market]["distance_km"]

        revenue = calculate_revenue(
            price,
            quantity_kg
        )

        transport_cost = calculate_transport_cost(
            distance,
            transport_rate
        )

        storage_cost = calculate_storage_cost(
            quantity_kg,
            storage_days,
            storage_rate
        )

        profit = calculate_net_profit(
            price,
            quantity_kg,
            transport_cost,
            storage_cost
        )

        results.append({
            "market": market,
            "date": date,
            "predicted_price": price,
            "revenue": revenue,
            "transport_cost": transport_cost,
            "storage_cost": storage_cost,
            "net_profit": profit
        })

    if not results:
        raise ValueError("No prediction data available")

    best = max(
        results,
        key=lambda x: x["net_profit"]
    )

    return {
        "recommended_market": best["market"],
        "recommended_date": best["date"],
        "predicted_price": best["predicted_price"],
        "transport_cost": best["transport_cost"],
        "storage_cost": best["storage_cost"],
        "expected_revenue": best["revenue"],
        "expected_profit": best["net_profit"],
        "all_options": results
    }