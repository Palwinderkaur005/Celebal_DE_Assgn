import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

queries = {

"Purchase Frequency": """

SELECT

customer_id,

COUNT(order_id)

AS Orders,

CASE

WHEN COUNT(order_id)=1

THEN 'One-Time'

WHEN COUNT(order_id)<=5

THEN 'Occasional'

ELSE 'Loyal'

END

AS Segment

FROM orders

GROUP BY customer_id;

""",

"Spend Tier": """

SELECT

c.customer_name,

ROUND(

SUM(

oi.quantity*
oi.unit_price*
(1-discount_percent/100.0)

),2)

AS Spend,

CASE

WHEN

SUM(

oi.quantity*
oi.unit_price*
(1-discount_percent/100.0)

)<50000

THEN 'Low'

WHEN

SUM(

oi.quantity*
oi.unit_price*
(1-discount_percent/100.0)

)<150000

THEN 'Medium'

ELSE 'High'

END

AS SpendTier

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY c.customer_name;

""",

"RFM Analysis": """

WITH RFM AS (

SELECT

o.customer_id,

MAX(order_date)

AS LastPurchase,

COUNT(DISTINCT o.order_id)

AS Frequency,

ROUND(

SUM(

oi.quantity*
oi.unit_price*
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

FROM RFM;

"""

}

for title, query in queries.items():

    print("\n" + "="*70)
    print(title)
    print("="*70)

    df = pd.read_sql(query, conn)

    print(df.head(20))

conn.close()