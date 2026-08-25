# ============================================================
# SALES & REVENUE ANALYTICS
# DATA CLEANING
# ============================================================

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/sales_transactions.csv")

print("Original Dataset Shape:", df.shape)

# Remove duplicate records
df = df.drop_duplicates()

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Handle missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with critical missing values
df = df.dropna(
    subset=[
        "Order ID",
        "Order Date",
        "Customer ID",
        "Product ID",
        "Sales",
        "Cost",
        "Profit"
    ]
)

# Validate numeric columns
numeric_columns = [
    "Quantity",
    "Unit Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove invalid transactions
df = df[df["Quantity"] > 0]
df = df[df["Unit Price"] >= 0]
df = df[df["Sales"] >= 0]
df = df[df["Cost"] >= 0]

# Recalculate Profit to ensure consistency
df["Calculated Profit"] = (
    df["Sales"] - df["Cost"]
).round(2)

# Compare calculated and existing profit
df["Profit Difference"] = (
    df["Profit"] - df["Calculated Profit"]
).round(2)

# Display cleaned dataset information
print("\nCleaned Dataset Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nDescriptive Statistics:")
print(df.describe())

# Save cleaned dataset
df.to_csv(
    "../data/cleaned_sales_transactions.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")
