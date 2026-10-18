import pandas as pd

# Load dataset
df = pd.read_csv("data/retail_business_sales.csv")

print("=== DATASET SHAPE ===")
print(df.shape)

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATE ROWS ===")
print(df.duplicated().sum())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== STATISTICAL SUMMARY ===")
print(df.describe())

print("\n=== FIRST 5 ROWS ===")
print(df.head())
print("\n=== CATEGORY-WISE SALES ===")
category_sales = df.groupby("Category")["Sales_Amount"].sum().sort_values(ascending=False)
print(category_sales)

print("\n=== CATEGORY-WISE PROFIT ===")
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print(category_profit)
print("\n=== REGION-WISE SALES ===")
region_sales = df.groupby("Region")["Sales_Amount"].sum().sort_values(ascending=False)
print(region_sales)

print("\n=== REGION-WISE PROFIT ===")
region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
print(region_profit)
print("\n=== TOP 10 PRODUCTS BY SALES ===")
top_products = (
    df.groupby("Product")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_products)