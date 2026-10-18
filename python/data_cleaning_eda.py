import pandas as pd

# Load dataset
df = pd.read_csv("data/retail_business_sales.csv")

# Basic information
print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

print("\n--- Statistical Summary ---")
print(df.describe())

print("\n--- First 5 Rows ---")
print(df.head())
# ==============================
# SALES & PROFIT ANALYSIS
# ==============================

print("\n=== SALES & PROFIT ANALYSIS ===")

print("\nTotal Sales:")
print(df["Sales_Amount"].sum())

print("\nTotal Cost:")
print(df["Total_Cost"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

print("\nAverage Sales per Order:")
print(df["Sales_Amount"].mean())

print("\nAverage Profit per Order:")
print(df["Profit"].mean())

print("\nMaximum Sales:")
print(df["Sales_Amount"].max())

print("\nMaximum Profit:")
print(df["Profit"].max())
# ==============================
# SALES & PROFIT ANALYSIS
# ==============================

print("\n=== SALES & PROFIT ANALYSIS ===")

# Total Sales
total_sales = df["Sales_Amount"].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Average Sales
average_sales = df["Sales_Amount"].mean()
print("Average Sales per Order:", average_sales)

# Average Profit
average_profit = df["Profit"].mean()
print("Average Profit per Order:", average_profit)

# Total Cost
total_cost = df["Total_Cost"].sum()
print("Total Cost:", total_cost)

# Profit Margin
profit_margin = (total_profit / total_sales) * 100
print("Profit Margin:", profit_margin)