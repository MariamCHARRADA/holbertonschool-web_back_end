-- Lists all bands with Glam rock as their main style, ranked by their longevity.
-- Column names: band_name and lifespan (in years)
-- Lifespan is calculated using the attributes `formed` and `split`.

SELECT band_name, COALESCE(split, 2020) - formed as lifespan
FROM metal_bands
WHERE
    style LIKE '%Glam rock%'