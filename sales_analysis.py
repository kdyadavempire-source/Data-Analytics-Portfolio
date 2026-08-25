# ============================================================
# SALES & REVENUE ANALYTICS
# Python Exploratory Data Analysis
# Author: Kunal Das Yadav
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv("../data/sales_transactions.csv")

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# ============================================================
# 2. DATA OVERVIEW
# ============================================================

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Statistical Summary ---")
print(df.describe())

# ============================================================
# 3. DATA CLEANING
# ============================================================

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Records ---")
print(df.duplicated().sum())

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Remove duplicate records
df = df.drop_duplicates()

# ============================================================
# 4. KPI CALCULATIONS
# ============================================================

total_revenue = df["Sales"].sum()
total_cost = df["Cost"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_quantity = df["Quantity"].sum()

average_order_value = total_revenue / total_orders

profit_margin = (total_profit / total_revenue) * 100

print("\n================ KPI SUMMARY ================")
print(f"Total Revenue       : ${total_revenue:,.2f}")
print(f"Total Cost          : ${total_cost:,.2f}")
print(f"Total Profit        : ${total_profit:,.2f}")
print(f"Total Orders        : {total_orders:,}")
print(f"Total Quantity      : {total_quantity:,}")
print(f"Average Order Value : ${average_order_value:,.2f}")
print(f"Profit Margin       : {profit_margin:.2f}%")

# ============================================================
# 5. PRODUCT ANALYSIS
# ============================================================

product_analysis = (
    df.groupby("Product Name")
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Top 10 Products by Revenue ---")
print(product_analysis.head(10))

# ============================================================
# 6. CATEGORY ANALYSIS
# ============================================================

category_analysis = (
    df.groupby("Category")
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Category Performance ---")
print(category_analysis)

# ============================================================
# 7. REGIONAL ANALYSIS
# ============================================================

regional_analysis = (
    df.groupby("Region")
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Regional Performance ---")
print(regional_analysis)

# ============================================================
# 8. CUSTOMER ANALYSIS
# ============================================================

customer_analysis = (
    df.groupby(["Customer ID", "Customer Name"])
      .agg(
          Revenue=("Sales", "sum"),
          Orders=("Order ID", "nunique"),
          Profit=("Profit", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Top 10 Customers ---")
print(customer_analysis.head(10))

# ============================================================
# 9. MONTHLY REVENUE TREND
# ============================================================

df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_revenue = (
    df.groupby("Year-Month")["Sales"]
      .sum()
      .reset_index()
)

print("\n--- Monthly Revenue ---")
print(monthly_revenue)

# ============================================================
# 10. YEARLY REVENUE
# ============================================================

yearly_revenue = (
    df.groupby(df["Order Date"].dt.year)["Sales"]
      .sum()
      .reset_index()
)

yearly_revenue.columns = ["Year", "Revenue"]

print("\n--- Yearly Revenue ---")
print(yearly_revenue)

# ============================================================
# 11. VISUALIZATION - MONTHLY REVENUE
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_revenue["Year-Month"],
    monthly_revenue["Sales"],
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# ============================================================
# 12. VISUALIZATION - CATEGORY REVENUE
# ============================================================

plt.figure(figsize=(10, 6))

category_analysis["Revenue"].plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# ============================================================
# 13. VISUALIZATION - REGIONAL REVENUE
# ============================================================

plt.figure(figsize=(10, 6))

regional_analysis["Revenue"].plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# ============================================================
# 14. CORRELATION ANALYSIS
# ============================================================

numeric_columns = [
    "Quantity",
    "Unit Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title("Sales Data Correlation Matrix")
plt.tight_layout()

plt.show()

# ============================================================
# 15. FINAL BUSINESS INSIGHTS
# ============================================================

top_product = product_analysis.index[0]
top_category = category_analysis.index[0]
top_region = regional_analysis.index[0]
top_customer = customer_analysis.index[0]

print("\n================ BUSINESS INSIGHTS ================")

print(f"Top Product   : {top_product}")
print(f"Top Category  : {top_category}")
print(f"Top Region    : {top_region}")
print(f"Top Customer  : {top_customer}")

print("\nPython analysis completed successfully!")
