import sqlite3
import pandas as pd
from tabulate import tabulate

conn = sqlite3.connect("database/ecommerce.db")

query = """
WITH FirstPurchase AS (

SELECT

customer_id,

MIN(
strftime('%Y-%m',order_date)
)

AS CohortMonth

FROM orders

GROUP BY customer_id

)

SELECT

FirstPurchase.CohortMonth,

strftime('%Y-%m',o.order_date)

AS PurchaseMonth,

COUNT(DISTINCT o.customer_id)

AS Customers

FROM orders o

JOIN FirstPurchase

ON o.customer_id=FirstPurchase.customer_id

GROUP BY

FirstPurchase.CohortMonth,

PurchaseMonth

ORDER BY

FirstPurchase.CohortMonth,

PurchaseMonth;
"""

df = pd.read_sql(query, conn)

print("\nCohort Analysis\n")

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

conn.close()