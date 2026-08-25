-- ============================================================
-- DATA VALIDATION & QUALITY CHECKS
-- ============================================================

USE sales_revenue_analytics;

-- Total transactions
SELECT COUNT(*) AS total_transactions
FROM sales_transactions;

-- Total customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Total products
SELECT COUNT(*) AS total_products
FROM products;

-- Check duplicate orders
SELECT order_id, COUNT(*) AS duplicate_count
FROM sales_transactions
GROUP BY order_id
HAVING COUNT(*) > 1;

-- Check missing values
SELECT
    SUM(order_id IS NULL) AS missing_order_id,
    SUM(order_date IS NULL) AS missing_order_date,
    SUM(customer_id IS NULL) AS missing_customer_id,
    SUM(product_id IS NULL) AS missing_product_id,
    SUM(category IS NULL) AS missing_category,
    SUM(region IS NULL) AS missing_region,
    SUM(quantity IS NULL) AS missing_quantity,
    SUM(sales IS NULL) AS missing_sales,
    SUM(cost IS NULL) AS missing_cost,
    SUM(profit IS NULL) AS missing_profit
FROM sales_transactions;

-- Check negative sales
SELECT *
FROM sales_transactions
WHERE sales < 0;

-- Check negative quantity
SELECT *
FROM sales_transactions
WHERE quantity <= 0;

-- Check profit calculation
SELECT
    order_id,
    sales,
    cost,
    profit,
    ROUND(sales - cost, 2) AS calculated_profit
FROM sales_transactions
LIMIT 20;
