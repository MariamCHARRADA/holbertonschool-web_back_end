-- Lists all bands with Glam rock as their main style, ranked by their longevity.
-- Column names: band_name and lifespan (in years)
-- Lifespan is calculated using the attributes `formed` and `split`.

SELECT band_name, IF(
        split IS NOT NULL, split - formed, 2022 - formed
    ) AS lifespan
FROM metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY lifespan DESC;