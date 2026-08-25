# ============================================================
# SALES & REVENUE ANALYTICS
# DATA VISUALIZATION
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_transactions.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create output folder
os.makedirs("../screenshots/python", exist_ok=True)

# ------------------------------------------------------------
# 1. Monthly Revenue Trend
# ------------------------------------------------------------

monthly_revenue = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "../screenshots/python/monthly_revenue.png",
    dpi=150
)

plt.show()


# ------------------------------------------------------------
# 2. Revenue by Category
# ------------------------------------------------------------

category_revenue = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
category_revenue.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    "../screenshots/python/revenue_by_category.png",
    dpi=150
)

plt.show()


# ------------------------------------------------------------
# 3. Revenue by Region
# ------------------------------------------------------------

region_revenue = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
region_revenue.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "../screenshots/python/revenue_by_region.png",
    dpi=150
)

plt.show()


# ------------------------------------------------------------
# 4. Top 10 Products by Revenue
# ------------------------------------------------------------

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(
    "../screenshots/python/top_10_products.png",
    dpi=150
)

plt.show()


# ------------------------------------------------------------
# 5. Profit by Category
# ------------------------------------------------------------

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    "../screenshots/python/profit_by_category.png",
    dpi=150
)

plt.show()


print("All visualizations created successfully.")
