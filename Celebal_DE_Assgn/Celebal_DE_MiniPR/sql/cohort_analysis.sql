-- ==========================================
-- QUERY 1
-- Customer First Purchase
-- ==========================================

SELECT

customer_id,

MIN(

strftime('%Y-%m',order_date)

)

AS First_Purchase

FROM orders

GROUP BY customer_id;

-- ==========================================
-- QUERY 2
-- Customer Cohorts
-- ==========================================

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

o.customer_id,

FirstPurchase.CohortMonth,

strftime('%Y-%m',o.order_date)

AS PurchaseMonth

FROM orders o

JOIN FirstPurchase

ON

o.customer_id=

FirstPurchase.customer_id

ORDER BY

FirstPurchase.CohortMonth;

-- ==========================================
-- QUERY 3
-- Retention Analysis
-- ==========================================

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

AS Active_Customers

FROM orders o

JOIN FirstPurchase

ON

o.customer_id=

FirstPurchase.customer_id

GROUP BY

FirstPurchase.CohortMonth,

PurchaseMonth

ORDER BY

FirstPurchase.CohortMonth,

PurchaseMonth;

-- ==========================================
-- QUERY 4
-- Repeat Customers
-- ==========================================

SELECT

customer_id,

COUNT(order_id)

AS TotalOrders

FROM orders

GROUP BY customer_id

HAVING

COUNT(order_id)>1

ORDER BY TotalOrders DESC;

-- ==========================================
-- QUERY 5
-- One Time Customers
-- ==========================================

SELECT

customer_id,

COUNT(order_id)

AS Orders

FROM orders

GROUP BY customer_id

HAVING Orders=1;

-- ==========================================
-- QUERY 6
-- Churned Customers
-- ==========================================

SELECT

customer_id,

COUNT(order_id)

AS Orders

FROM orders

GROUP BY customer_id

HAVING COUNT(order_id)=1;

