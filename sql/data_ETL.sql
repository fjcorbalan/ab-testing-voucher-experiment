-- User-level experiment outcome table
-- One row per user per experiment

WITH experiment_users AS (
    SELECT
        user_id,
        variant
    FROM experiment_assignments
    WHERE experiment_id = 'voucher_ui_01'
),

exposed_users AS (
    SELECT DISTINCT
        eu.user_id,
        eu.variant
    FROM experiment_users eu
    JOIN events e
      ON eu.user_id = e.user_id
    WHERE e.event_name = 'product_viewed'
),

user_redemptions AS (
    SELECT
        ex.user_id,
        ex.variant,
        CASE
            WHEN COUNT(o.order_id) > 0 THEN 1
            ELSE 0
        END AS redeemed
    FROM exposed_users ex
    LEFT JOIN orders o
      ON ex.user_id = o.user_id
     AND o.voucher_id IS NOT NULL
    GROUP BY 1, 2
)

SELECT *
FROM user_redemptions;
