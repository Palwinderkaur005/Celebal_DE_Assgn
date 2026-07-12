import sqlite3
import pandas as pd
from tabulate import tabulate

# Connect to database
conn = sqlite3.connect("database/ecommerce.db")

query = """
SELECT
    p.category,
    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount_percent/100.0)
        ),2
    ) AS Revenue

FROM products p

JOIN order_items oi
ON p.product_id = oi.product_id

GROUP BY p.category

ORDER BY Revenue DESC;
"""

df = pd.read_sql(query, conn)

print("\nRevenue By Category\n")
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

conn.close()