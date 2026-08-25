# ============================================================
# SALES & REVENUE ANALYTICS
# EXPLORATORY DATA ANALYSIS
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_transactions.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Dataset overview
print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

# KPI Analysis
total_revenue = df["Sales"].sum()
total_cost = df["Cost"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_revenue / total_orders
profit_margin = (total_profit / total_revenue) * 100

print("\n========== KEY PERFORMANCE INDICATORS ==========")
print("Total Revenue:", round(total_revenue, 2))
print("Total Cost:", round(total_cost, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Quantity:", total_quantity)
print("Average Order Value:", round(average_order_value, 2))
print("Profit Margin:", round(profit_margin, 2), "%")

# Product Analysis
product_analysis = (
    df.groupby("Product Name")
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

print("\n========== TOP PRODUCTS ==========")
print(product_analysis.head(10))

# Category Analysis
category_analysis = (
    df.groupby("Category")
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

print("\n========== CATEGORY PERFORMANCE ==========")
print(category_analysis)

# Regional Analysis
regional_analysis = (
    df.groupby("Region")
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

print("\n========== REGIONAL PERFORMANCE ==========")
print(regional_analysis)

# Monthly Revenue
monthly_revenue = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print("\n========== MONTHLY REVENUE ==========")
print(monthly_revenue)

# Customer Analysis
customer_analysis = (
    df.groupby(["Customer ID", "Customer Name"])
    .agg(
        Orders=("Order ID", "nunique"),
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

print("\n========== TOP CUSTOMERS ==========")
print(customer_analysis.head(10))

print("\nEDA completed successfully.")
