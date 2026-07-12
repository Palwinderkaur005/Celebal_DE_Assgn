import sqlite3
import pandas as pd
import os

# -----------------------------
# Create database folder
# -----------------------------
os.makedirs("database", exist_ok=True)

# -----------------------------
# Connect Database
# -----------------------------
conn = sqlite3.connect("database/ecommerce.db")

cursor = conn.cursor()

print("Database Connected")

# -----------------------------
# Read schema.sql
# -----------------------------
with open("sql/schema.sql", "r") as file:
    sql_script = file.read()

cursor.executescript(sql_script)

print("Tables Created")

# -----------------------------
# Read Cleaned CSVs
# -----------------------------

customers = pd.read_csv("data/cleaned/customers_clean.csv")

products = pd.read_csv("data/cleaned/products_clean.csv")

orders = pd.read_csv("data/cleaned/orders_clean.csv")

order_items = pd.read_csv("data/cleaned/order_items_clean.csv")

# -----------------------------
# Insert Data
# -----------------------------

customers.to_sql(
    "customers",
    conn,
    if_exists="append",
    index=False
)

products.to_sql(
    "products",
    conn,
    if_exists="append",
    index=False
)

orders.to_sql(
    "orders",
    conn,
    if_exists="append",
    index=False
)

order_items.to_sql(
    "order_items",
    conn,
    if_exists="append",
    index=False
)

print("Data Inserted Successfully")

# -----------------------------
# Verify Row Counts
# -----------------------------

tables = [
    "customers",
    "products",
    "orders",
    "order_items"
]

print("\nRow Counts\n")

for table in tables:

    query = f"SELECT COUNT(*) FROM {table}"

    cursor.execute(query)

    count = cursor.fetchone()[0]

    print(f"{table} : {count}")

conn.commit()

conn.close()

print("\nDatabase Closed")