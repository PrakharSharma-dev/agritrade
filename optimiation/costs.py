# costs.py

def kg_to_quintals(quantity_kg):
    return quantity_kg / 100


def calculate_revenue(predicted_price, quantity_kg):
    quantity_quintals = kg_to_quintals(quantity_kg)

    return predicted_price * quantity_quintals


def calculate_transport_cost(distance_km, rate_per_km):
    return distance_km * rate_per_km


def calculate_storage_cost(
    quantity_kg,
    storage_days,
    rate_per_kg_per_day
):
    return quantity_kg * storage_days * rate_per_kg_per_day


def calculate_net_profit(
    predicted_price,
    quantity_kg,
    transport_cost,
    storage_cost
):
    revenue = calculate_revenue(
        predicted_price,
        quantity_kg
    )

    return revenue - transport_cost - storage_cost
