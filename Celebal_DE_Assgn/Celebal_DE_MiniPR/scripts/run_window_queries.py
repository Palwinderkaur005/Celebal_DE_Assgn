import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

queries = {

"Customer Ranking": """
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
) DESC
)
AS Rank
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_name;
""",

"Running Total": """
SELECT
Month,
Revenue,

SUM(Revenue)
OVER(
ORDER BY Month
)
AS Running_Total

FROM(

SELECT
strftime('%Y-%m',order_date)
AS Month,

SUM(
quantity*
unit_price*
(1-discount_percent/100.0)
)
AS Revenue

FROM orders
JOIN order_items
USING(order_id)

GROUP BY Month
);
"""
}

for title, query in queries.items():

    print("="*70)
    print(title)
    print("="*70)

    df = pd.read_sql(query, conn)

    print(df)

conn.close()