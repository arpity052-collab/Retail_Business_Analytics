import pandas as pd
import numpy as np

# Number of records
NUMBER_OF_RECORDS = 50000

# Same random results every time
np.random.seed(42)

# Customer information
customer_names = [
    "Aarav Sharma", "Vivaan Verma", "Aditya Singh",
    "Arjun Gupta", "Rahul Yadav", "Rohan Mishra",
    "Ananya Sharma", "Priya Singh", "Sneha Gupta",
    "Neha Verma", "Pooja Yadav", "Kavya Mishra",
    "Riya Singh", "Aditi Gupta", "Simran Sharma"
]

genders = ["Male", "Female"]

# Indian locations
locations = [
    ("Lucknow", "Uttar Pradesh", "North"),
    ("Kanpur", "Uttar Pradesh", "North"),
    ("Delhi", "Delhi", "North"),
    ("Jaipur", "Rajasthan", "North"),
    ("Chandigarh", "Chandigarh", "North"),
    ("Mumbai", "Maharashtra", "West"),
    ("Pune", "Maharashtra", "West"),
    ("Ahmedabad", "Gujarat", "West"),
    ("Surat", "Gujarat", "West"),
    ("Bengaluru", "Karnataka", "South"),
    ("Chennai", "Tamil Nadu", "South"),
    ("Hyderabad", "Telangana", "South"),
    ("Kochi", "Kerala", "South"),
    ("Kolkata", "West Bengal", "East"),
    ("Bhubaneswar", "Odisha", "East")
]

# Generate customer IDs
customer_ids = [
    f"CUST{i:05d}"
    for i in range(1, 10001)
]

# Generate random customer information
customer_data = {
    "Customer_ID": np.random.choice(
        customer_ids, NUMBER_OF_RECORDS
    ),

    "Customer_Name": np.random.choice(
        customer_names, NUMBER_OF_RECORDS
    ),

    "Gender": np.random.choice(
        genders, NUMBER_OF_RECORDS
    ),

    "Age": np.random.randint(
        18, 61, NUMBER_OF_RECORDS
    )
}

# Generate location information
selected_locations = np.random.choice(
    len(locations),
    NUMBER_OF_RECORDS
)

customer_data["City"] = [
    locations[i][0] for i in selected_locations
]

customer_data["State"] = [
    locations[i][1] for i in selected_locations
]

customer_data["Region"] = [
    locations[i][2] for i in selected_locations
]

# Convert to DataFrame
df = pd.DataFrame(customer_data)

print("Customer and location data created successfully!")
print(f"Records: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nFirst 5 records:")
print(df.head())
# -------------------------------
# PHASE 2: PRODUCT & SALES DATA
# -------------------------------

# Product catalogue
products = [
    ("P001", "Laptop", "Electronics", 55000, 42000),
    ("P002", "Smartphone", "Electronics", 25000, 18000),
    ("P003", "Headphones", "Electronics", 2500, 1400),
    ("P004", "Smartwatch", "Electronics", 4500, 2800),
    ("P005", "Keyboard", "Electronics", 1800, 1000),
    ("P006", "T-Shirt", "Fashion", 999, 500),
    ("P007", "Jeans", "Fashion", 1999, 1100),
    ("P008", "Shoes", "Fashion", 2999, 1700),
    ("P009", "Backpack", "Fashion", 1499, 800),
    ("P010", "Coffee Maker", "Home", 4999, 3000),
    ("P011", "Mixer Grinder", "Home", 3499, 2100),
    ("P012", "Bedsheet", "Home", 1299, 700),
    ("P013", "Office Chair", "Furniture", 7999, 5000),
    ("P014", "Study Table", "Furniture", 6499, 4000),
    ("P015", "Bookshelf", "Furniture", 5499, 3300),
]

# Randomly select products
selected_products = np.random.randint(
    0, len(products), NUMBER_OF_RECORDS
)

df["Product_ID"] = [
    products[i][0] for i in selected_products
]

df["Product"] = [
    products[i][1] for i in selected_products
]

df["Category"] = [
    products[i][2] for i in selected_products
]

df["Unit_Price"] = [
    products[i][3] for i in selected_products
]

df["Cost_Price"] = [
    products[i][4] for i in selected_products
]

# Order information
df["Order_ID"] = [
    f"ORD{i:06d}"
    for i in range(1, NUMBER_OF_RECORDS + 1)
]

# Order dates
df["Order_Date"] = pd.to_datetime(
    np.random.choice(
        pd.date_range("2025-01-01", "2026-09-30"),
        NUMBER_OF_RECORDS
    )
)

# Quantity sold
df["Quantity"] = np.random.randint(
    1, 6, NUMBER_OF_RECORDS
)

# Discount percentage
df["Discount"] = np.random.choice(
    [0, 5, 10, 15, 20],
    NUMBER_OF_RECORDS
)

# Sales amount before discount
df["Gross_Sales"] = (
    df["Quantity"] * df["Unit_Price"]
)

# Discount amount
df["Discount_Amount"] = (
    df["Gross_Sales"] * df["Discount"] / 100
)

# Final sales amount
df["Sales_Amount"] = (
    df["Gross_Sales"] - df["Discount_Amount"]
)

# Total cost
df["Total_Cost"] = (
    df["Quantity"] * df["Cost_Price"]
)

# Profit
df["Profit"] = (
    df["Sales_Amount"] - df["Total_Cost"]
)

# Payment methods
df["Payment_Mode"] = np.random.choice(
    ["UPI", "Credit Card", "Debit Card", "Cash", "Net Banking"],
    NUMBER_OF_RECORDS
)

# Order status
df["Order_Status"] = np.random.choice(
    ["Delivered", "Delivered", "Delivered", "Cancelled", "Returned"],
    NUMBER_OF_RECORDS
)

# Final dataset information
print("\nPhase 2 completed successfully!")
print(f"Total Records: {len(df)}")
print(f"Total Columns: {len(df.columns)}")

print("\nAll columns:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())
# Save final dataset
output_path = "data/retail_business_sales.csv"
df.to_csv(output_path,index=False)
print("\nDataset saved successfully!")
print(f"File saved at:{output_path}")