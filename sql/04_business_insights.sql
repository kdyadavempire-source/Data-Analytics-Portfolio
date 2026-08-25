-- ============================================================
-- BUSINESS INSIGHTS
-- ============================================================

USE sales_revenue_analytics;

-- Revenue contribution by category
SELECT
    category,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(
        SUM(sales) * 100 /
        (SELECT SUM(sales) FROM sales_transactions),
        2
    ) AS revenue_percentage
FROM sales_transactions
GROUP BY category
ORDER BY revenue DESC;

-- Profit margin by category
SELECT
    category,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit,
    ROUND(SUM(profit) * 100 / SUM(sales), 2) AS profit_margin
FROM sales_transactions
GROUP BY category
ORDER BY profit_margin DESC;

-- Regional performance
SELECT
    region,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit,
    ROUND(SUM(profit) * 100 / SUM(sales), 2) AS profit_margin
FROM sales_transactions
GROUP BY region
ORDER BY revenue DESC;

-- Best performing month
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    ROUND(SUM(sales), 2) AS revenue
FROM sales_transactions
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY revenue DESC
LIMIT 1;

-- Highest profit product
SELECT
    product_name,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_transactions
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 1;
