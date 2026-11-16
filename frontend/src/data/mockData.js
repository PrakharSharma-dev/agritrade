/**
 * Mock data for AgriTrade frontend.
 * This structure reflects the exact response contract expected from the backend FastAPI service.
 * The frontend does NOT calculate or derive recommendations; it only consumes this payload.
 */

export const MOCK_RECOMMENDATION_RESPONSE = {
  crop: "Wheat",
  farmer_location: "Ajmer",
  quantity: 1000, // kg
  current_price: 2350, // ₹ / quintal

  forecast: [
    { day: "Day 1", date: "2026-09-01", predicted_price: 2380 },
    { day: "Day 2", date: "2026-09-02", predicted_price: 2410 },
    { day: "Day 3", date: "2026-09-03", predicted_price: 2450 },
    { day: "Day 4", date: "2026-09-04", predicted_price: 2490 },
    { day: "Day 5", date: "2026-09-05", predicted_price: 2520 },
    { day: "Day 6", date: "2026-09-06", predicted_price: 2500 },
    { day: "Day 7", date: "2026-09-07", predicted_price: 2480 }
  ],

  markets: [
    {
      market: "Ajmer Mandi",
      location: "Ajmer",
      distance_km: 12,
      predicted_price: 2380,
      is_recommended: false
    },
    {
      market: "Jaipur Mandi",
      location: "Jaipur",
      distance_km: 135,
      predicted_price: 2520,
      is_recommended: true
    },
    {
      market: "Kishangarh Mandi",
      location: "Kishangarh",
      distance_km: 32,
      predicted_price: 2460,
      is_recommended: false
    },
    {
      market: "Kota Mandi",
      location: "Kota",
      distance_km: 210,
      predicted_price: 2490,
      is_recommended: false
    }
  ],

  recommendation: {
    market: "Jaipur Mandi",
    date: "5 September 2026",
    raw_date: "2026-09-05",
    predicted_price: 2520,
    transport_cost: 2000,
    storage_cost: 500,
    total_cost: 2500,
    expected_profit: 22500,
    reasoning: "Based on the predicted prices and estimated costs, AgriTrade recommends selling at Jaipur Mandi on 5 September."
  }
};

export const AVAILABLE_CROPS = [
  { id: "Wheat", name: "Wheat (गेहूं)", icon: "🌾", defaultPrice: 2350 },
  { id: "Mustard", name: "Mustard (सरसों)", icon: "🌱", defaultPrice: 5400 },
  { id: "Gram", name: "Gram / Chana (चना)", icon: "🌿", defaultPrice: 5850 },
  { id: "Soybean", name: "Soybean (सोयाबीन)", icon: "🍃", defaultPrice: 4600 },
  { id: "Cotton", name: "Cotton (कपास)", icon: "☁️", defaultPrice: 7100 }
];

export const AVAILABLE_LOCATIONS = [
  "Ajmer",
  "Jaipur",
  "Kishangarh",
  "Kota",
  "Bhilwara",
  "Tonk",
  "Alwar"
];
