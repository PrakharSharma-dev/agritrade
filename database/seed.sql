-- ============================================================
-- AgriTrade Seed Data
-- Version: 1.0 MVP
-- ============================================================

INSERT INTO crops (crop_name)
VALUES
    ('Wheat'),
    ('Mustard'),
    ('Onion'),
    ('Potato'),
    ('Tomato')
ON CONFLICT (crop_name) DO NOTHING;
SELECT
    table_name,
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name IN ('crops', 'markets', 'market_prices')
ORDER BY table_name, ordinal_position;