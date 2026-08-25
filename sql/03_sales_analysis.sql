-- ============================================================
-- SALES & REVENUE ANALYSIS
-- ============================================================

USE sales_revenue_analytics;

-- 1. Total Revenue
SELECT
    ROUND(SUM(sales), 2) AS total_revenue
FROM sales_transactions;

-- 2. Total Cost
SELECT
    ROUND(SUM(cost), 2) AS total_cost
FROM sales_transactions;

-- 3. Total Profit
SELECT
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_transactions;

-- 4. Total Orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM sales_transactions;

-- 5. Total Quantity Sold
SELECT
    SUM(quantity) AS total_quantity
FROM sales_transactions;

-- 6. Average Order Value
SELECT
    ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2)
        AS average_order_value
FROM sales_transactions;

-- 7. Sales by Category
SELECT
    category,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM sales_transactions
GROUP BY category
ORDER BY revenue DESC;

-- 8. Sales by Region
SELECT
    region,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM sales_transactions
GROUP BY region
ORDER BY revenue DESC;

-- 9. Top 10 Products
SELECT
    product_name,
    category,
    SUM(quantity) AS quantity_sold,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM sales_transactions
GROUP BY product_name, category
ORDER BY revenue DESC
LIMIT 10;

-- 10. Monthly Revenue
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    ROUND(SUM(sales), 2) AS revenue
FROM sales_transactions
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;

-- 11. Yearly Revenue
SELECT
    YEAR(order_date) AS year,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM sales_transactions
GROUP BY YEAR(order_date)
ORDER BY year;

-- 12. Top Customers
SELECT
    customer_id,
    customer_name,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(sales), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM sales_transactions
GROUP BY customer_id, customer_name
ORDER BY revenue DESC
LIMIT 10;
