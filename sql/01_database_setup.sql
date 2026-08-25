-- ============================================================
-- SALES & REVENUE ANALYTICS
-- Database Setup
-- Author: Kunal Das Yadav
-- ============================================================

CREATE DATABASE IF NOT EXISTS sales_revenue_analytics;

USE sales_revenue_analytics;

-- ============================================================
-- PRODUCTS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2),
    unit_cost DECIMAL(10,2)
);

-- ============================================================
-- CUSTOMERS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100)
);

-- ============================================================
-- SALES TRANSACTIONS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS sales_transactions (
    order_id VARCHAR(20) PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    product_id VARCHAR(20),
    product_name VARCHAR(100),
    category VARCHAR(50),
    region VARCHAR(30),
    quantity INT,
    unit_price DECIMAL(10,2),
    discount DECIMAL(5,2),
    sales DECIMAL(12,2),
    cost DECIMAL(12,2),
    profit DECIMAL(12,2)
);

-- ============================================================
-- VERIFY TABLES
-- ============================================================

SHOW TABLES;
