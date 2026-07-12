import pandas as pd
import numpy as np
from datetime import datetime
import os
os.makedirs("data/cleaned", exist_ok=True)

#  Load all CSV files
customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
orders = pd.read_csv("data/raw/orders.csv")
order_items = pd.read_csv("data/raw/order_items.csv")

# Print Dataset Information
print("="*60)
print("RAW DATA INFORMATION")
print("="*60)

print("Customers :", customers.shape)
print("Products :", products.shape)
print("Orders :", orders.shape)
print("Order Items :", order_items.shape)

# Remove Duplicate Records
customers.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)
order_items.drop_duplicates(inplace=True)

print("\nDuplicates Removed")

# Check Missing Values
print("\nMissing Values")

print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())
print(order_items.isnull().sum())

# Fix Invalid Emails
customers = customers[
    customers["email"].str.contains("@", na=False)
]
print("\nCustomers after removing invalid emails :", len(customers))

# Clean Product Names
products["product_name"] = (
    products["product_name"]
    .str.strip()
    .str.title()
)

# Remove Future Order Dates
orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)
today = pd.Timestamp.today()

orders = orders[
    orders["order_date"] <= today
]

# Remove Orders Without Customer ID
orders = orders[
    orders["customer_id"].notna()
]

# Validate Customer IDs
valid_customers = set(customers["customer_id"])

orders = orders[
    orders["customer_id"].isin(valid_customers)
]

# Validate Order IDs
valid_orders = set(orders["order_id"])

order_items = order_items[
    order_items["order_id"].isin(valid_orders)
]

# Validate Product IDs
valid_products = set(products["product_id"])

order_items = order_items[
    order_items["product_id"].isin(valid_products)
]

# Remove Invalid Quantities
order_items = order_items[
    order_items["quantity"] > 0
]

# Remove Invalid Discounts
order_items = order_items[
    order_items["discount_percent"] <= 100
]

# Save Cleaned CSVs
customers.to_csv(
    "data/cleaned/customers_clean.csv",
    index=False
)

products.to_csv(
    "data/cleaned/products_clean.csv",
    index=False
)

orders.to_csv(
    "data/cleaned/orders_clean.csv",
    index=False
)

order_items.to_csv(
    "data/cleaned/order_items_clean.csv",
    index=False
)

# Print Summary
print("\nCleaning Completed Successfully!")

print("\nFinal Rows")

print("Customers :", len(customers))
print("Products :", len(products))
print("Orders :", len(orders))
print("Order Items :", len(order_items))

