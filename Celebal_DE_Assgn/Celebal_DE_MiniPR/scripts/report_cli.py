import sqlite3
import argparse
import pandas as pd
from tabulate import tabulate
import sys
import os


# =====================================
# Database Connection
# =====================================

DATABASE = "database/ecommerce.db"


def connect_database():

    if not os.path.exists(DATABASE):

        print("Database not found.")

        sys.exit()

    return sqlite3.connect(DATABASE)


# =====================================
# Revenue Report
# =====================================

def revenue_report(conn):

    query = """

    SELECT

    ROUND(

    SUM(

    quantity*
    unit_price*
    (1-discount_percent/100.0)

    ),2)

    AS TotalRevenue

    FROM order_items;

    """

    return pd.read_sql(query, conn)


# =====================================
# Top Customers
# =====================================

def top_customers(conn):

    query = """

    SELECT

    c.customer_name,

    ROUND(

    SUM(

    oi.quantity*
    oi.unit_price*
    (1-discount_percent/100.0)

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

    """

    return pd.read_sql(query, conn)


# =====================================
# Retention
# =====================================

def retention(conn):

    query = """

    WITH FirstPurchase AS (

    SELECT

    customer_id,

    MIN(

    strftime('%Y-%m',order_date)

    )

    AS Cohort

    FROM orders

    GROUP BY customer_id

    )

    SELECT

    Cohort,

    COUNT(*) AS Customers

    FROM FirstPurchase

    GROUP BY Cohort;

    """

    return pd.read_sql(query, conn)


# =====================================
# RFM
# =====================================

def rfm(conn):

    query = """

    WITH RFM AS(

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

    FROM RFM

    LIMIT 20;

    """

    return pd.read_sql(query, conn)


# =====================================
# Main Program
# =====================================

parser = argparse.ArgumentParser()

parser.add_argument(

"--report",

required=True,

help="Choose report"

)

args = parser.parse_args()

conn = connect_database()

if args.report=="revenue":

    df=revenue_report(conn)

elif args.report=="top_customers":

    df=top_customers(conn)

elif args.report=="retention":

    df=retention(conn)

elif args.report=="rfm":

    df=rfm(conn)

else:

    print("\nInvalid Report Name\n")

    print("Available Reports")

    print("---------------------")

    print("revenue")

    print("top_customers")

    print("retention")

    print("rfm")

    conn.close()

    sys.exit()

if df.empty:

    print("No Data Available")

else:

    print(tabulate(df,headers="keys",tablefmt="grid",showindex=False))

conn.close()