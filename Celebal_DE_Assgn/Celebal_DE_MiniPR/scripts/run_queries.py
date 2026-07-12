import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

queries = {

"1. Total Revenue": """
SELECT
ROUND(
SUM(
quantity*unit_price*
(1-discount_percent/100.0)
),2)
AS Total_Revenue
FROM order_items;
""",

"2. Revenue Per Customer": """
SELECT

c.customer_name,

ROUND(
SUM(
oi.quantity*
oi.unit_price*
(1-oi.discount_percent/100.0)
),2)

AS Revenue

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY c.customer_name

ORDER BY Revenue DESC

LIMIT 10;
""",

"3. Revenue Per Category": """
SELECT

p.category,

ROUND(
SUM(
oi.quantity*
oi.unit_price*
(1-discount_percent/100.0)
),2)

AS Revenue

FROM products p

JOIN order_items oi

ON p.product_id=oi.product_id

GROUP BY p.category;
""",

"4. Monthly Revenue": """
SELECT

strftime('%Y-%m',order_date)

AS Month,

ROUND(

SUM(
quantity*
unit_price*
(1-discount_percent/100.0)
),2)

AS Revenue

FROM orders

JOIN order_items

USING(order_id)

GROUP BY Month;
""",

"5. Orders Per Region": """
SELECT

region,

COUNT(*)

AS Orders

FROM orders

GROUP BY region;
"""

}

for title, query in queries.items():

    print("\n" + "="*70)
    print(title)
    print("="*70)

    df = pd.read_sql(query, conn)

    print(df)

conn.close()