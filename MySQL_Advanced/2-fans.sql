-- Ranks country origins of bands based on the total number of (non-unique) fans.
-- Column names: origin and nb_fans
-- Ordered by the number of fans in descending order.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY
    origin
ORDER BY nb_fans DESC;