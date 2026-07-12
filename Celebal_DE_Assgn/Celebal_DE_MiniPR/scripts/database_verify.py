import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

tables = [
    "customers",
    "products",
    "orders",
    "order_items"
]

for table in tables:

    print("=" * 60)

    print(table.upper())

    print("=" * 60)

    query = f"SELECT * FROM {table} LIMIT 5"

    df = pd.read_sql(query, conn)

    print(df)

conn.close()