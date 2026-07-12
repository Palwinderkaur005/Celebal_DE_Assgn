import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

queries = {

"Customer First Purchase": """

SELECT

customer_id,

MIN(

strftime('%Y-%m',order_date)

)

AS FirstPurchase

FROM orders

GROUP BY customer_id;

""",

"Repeat Customers": """

SELECT

customer_id,

COUNT(order_id)

AS Orders

FROM orders

GROUP BY customer_id

HAVING COUNT(order_id)>1

ORDER BY Orders DESC;

""",

"One Time Customers": """

SELECT

customer_id,

COUNT(order_id)

AS Orders

FROM orders

GROUP BY customer_id

HAVING COUNT(order_id)=1;

""",

"Retention": """

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

ON

o.customer_id=

FirstPurchase.customer_id

GROUP BY

FirstPurchase.CohortMonth,

PurchaseMonth;

"""

}

for title, query in queries.items():

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    df = pd.read_sql(query, conn)

    print(df)

conn.close()