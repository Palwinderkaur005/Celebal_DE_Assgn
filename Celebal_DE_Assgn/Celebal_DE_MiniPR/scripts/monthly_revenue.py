import sqlite3
import pandas as pd
from tabulate import tabulate

conn = sqlite3.connect("database/ecommerce.db")

query = """
SELECT

strftime('%Y-%m',o.order_date) AS Month,

ROUND(
SUM(
oi.quantity *
oi.unit_price *
(1-discount_percent/100.0)
),2)

AS Revenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY Month

ORDER BY Month;
"""

df = pd.read_sql(query, conn)

print("\nMonthly Revenue\n")
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

conn.close()