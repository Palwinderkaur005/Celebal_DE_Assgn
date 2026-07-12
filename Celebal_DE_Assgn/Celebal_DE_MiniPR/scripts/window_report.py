import sqlite3
import pandas as pd
from tabulate import tabulate

conn = sqlite3.connect("database/ecommerce.db")

query = """
SELECT
c.customer_name,

ROUND(
SUM(
oi.quantity *
oi.unit_price *
(1-discount_percent/100.0)
),2)

AS Revenue,

RANK()

OVER(

ORDER BY

SUM(
oi.quantity *
oi.unit_price *
(1-discount_percent/100.0)
)

DESC

)

AS Rank

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY c.customer_name;
"""

df = pd.read_sql(query, conn)

print("\nCustomer Ranking\n")

print(tabulate(df.head(20), headers="keys", tablefmt="grid", showindex=False))

conn.close()