import sqlite3
import pandas as pd
from tabulate import tabulate

conn = sqlite3.connect("database/ecommerce.db")

query = """
WITH RFM AS (

SELECT

o.customer_id,

MAX(order_date)

AS LastPurchase,

COUNT(DISTINCT o.order_id)

AS Frequency,

ROUND(

SUM(

oi.quantity *
oi.unit_price *
(1-discount_percent/100.0)

),2)

AS Monetary

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY o.customer_id

)

SELECT

customer_id,

ROUND(
julianday('now')
-
julianday(LastPurchase)
)

AS Recency,

Frequency,

Monetary

FROM RFM

ORDER BY Monetary DESC;
"""

df = pd.read_sql(query, conn)

print("\nRFM Analysis\n")

print(tabulate(df.head(20), headers="keys", tablefmt="grid", showindex=False))

conn.close()