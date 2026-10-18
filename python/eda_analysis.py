import pandas as pd

# Load dataset
df = pd.read_csv("../data/retail_business_sales.csv")

# Dataset shape
print("=== DATASET SHAPE ===")
print(df.shape)

# Column names
print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

# Missing values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Duplicate rows
print("\n=== DUPLICATE ROWS ===")
print(df.duplicated().sum())

# Category-wise sales
category_sales = df.groupby("Category")["Sales_Amount"].sum().sort_values(ascending=False)

print("\n=== CATEGORY-WISE SALES ===")
print(category_sales)
import matplotlib.pyplot as plt

# Category-wise Sales Visualization
category_sales.plot(kind="bar", figsize=(10, 6))

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Category-wise Profit
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

print("\n=== CATEGORY-WISE PROFIT ===")
print(category_profit)

# Visualization
category_profit.plot(kind="bar", figsize=(10, 6))

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# ==============================
# REGION-WISE SALES
# ==============================

region_sales = df.groupby("Region")["Sales_Amount"].sum().sort_values(ascending=False)

print("\n=== REGION-WISE SALES ===")
print(region_sales)

region_sales.plot(kind="bar", figsize=(8,5))

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==============================
# REGION-WISE PROFIT
# ==============================

region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

print("\n=== REGION-WISE PROFIT ===")
print(region_profit)

region_profit.plot(kind="bar", figsize=(8,5))

plt.title("Region-wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# MONTHLY SALES TREND
# ==============================

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Sales_Amount"].sum()

print("\n=== MONTHLY SALES ===")
print(monthly_sales)

monthly_sales.plot(
    kind="line",
    figsize=(10,5),
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# PAYMENT MODE ANALYSIS
# ==============================

payment_sales = df.groupby("Payment_Mode")["Sales_Amount"].sum().sort_values(ascending=False)

print("\n=== PAYMENT MODE SALES ===")
print(payment_sales)

payment_sales.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Sales by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# ORDER STATUS ANALYSIS
# ==============================

order_status = df["Order_Status"].value_counts()

print("\n=== ORDER STATUS ===")
print(order_status)

order_status.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# TOP 10 PRODUCTS BY SALES
# ==============================

product_sales = (
    df.groupby("Product")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n=== TOP 10 PRODUCTS BY SALES ===")
print(product_sales)

product_sales.plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# TOP 10 PRODUCTS BY PROFIT
# ==============================

product_profit = (
    df.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n=== TOP 10 PRODUCTS BY PROFIT ===")
print(product_profit)

product_profit.plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 10 Products by Profit")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# GENDER-WISE SALES
# ==============================

gender_sales = (
    df.groupby("Gender")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== GENDER-WISE SALES ===")
print(gender_sales)

gender_sales.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Gender-wise Sales")
plt.xlabel("Gender")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())
# ==============================
# AGE GROUP-WISE SALES
# ==============================

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 25, 35, 45, 55, 100],
    labels=["0-18", "19-25", "26-35", "36-45", "46-55", "56+"]
)

age_group_sales = (
    df.groupby("Age_Group", observed=True)["Sales_Amount"]
    .sum()
)

print("\n=== AGE GROUP-WISE SALES ===")
print(age_group_sales)

age_group_sales.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Age Group-wise Sales")
plt.xlabel("Age Group")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# ==============================
# TOP 10 CUSTOMERS BY SALES
# ==============================

top_customers = (
    df.groupby("Customer_Name")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n=== TOP 10 CUSTOMERS BY SALES ===")
print(top_customers)

top_customers.plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
# ==============================
# TOP 10 CUSTOMERS BY PROFIT
# ==============================

top_profit_customers = (
    df.groupby("Customer_Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n=== TOP 10 CUSTOMERS BY PROFIT ===")
print(top_profit_customers)

top_profit_customers.plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 10 Customers by Profit")
plt.xlabel("Customer")
plt.ylabel("Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
# ==============================
# REGION-WISE CUSTOMER COUNT
# ==============================

region_customers = (
    df.groupby("Region")["Customer_ID"]
    .nunique()
    .sort_values(ascending=False)
)

print("\n=== REGION-WISE CUSTOMER COUNT ===")
print(region_customers)

region_customers.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Region-wise Customer Count")
plt.xlabel("Region")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# ==============================
# CATEGORY-WISE PROFIT MARGIN
# ==============================

category_profit = df.groupby("Category")["Profit"].sum()
category_sales = df.groupby("Category")["Sales_Amount"].sum()

category_margin = (
    (category_profit / category_sales) * 100
).sort_values(ascending=False)
print("\n=== CATEGORY-WISE PROFIT MARGIN ===")
print(category_margin)

category_margin.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Category-wise Profit Margin")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# ==============================
# DISCOUNT VS PROFIT ANALYSIS
# ==============================

discount_profit = (
    df.groupby("Discount")["Profit"]
    .mean()
    .sort_index()
)

print("\n=== DISCOUNT VS AVERAGE PROFIT ===")
print(discount_profit)

discount_profit.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Discount vs Average Profit")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# ==============================
# ORDER STATUS-WISE PROFIT
# ==============================

status_profit = (
    df.groupby("Order_Status")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== ORDER STATUS-WISE PROFIT ===")
print(status_profit)

status_profit.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Order Status-wise Profit")
plt.xlabel("Order Status")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# MONTHLY PROFIT TREND
# ==============================

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_profit = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Profit"]
    .sum()
)

print("\n=== MONTHLY PROFIT TREND ===")
print(monthly_profit)

monthly_profit.plot(
    kind="line",
    figsize=(10, 5),
    marker="o"
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()