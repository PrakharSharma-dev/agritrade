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