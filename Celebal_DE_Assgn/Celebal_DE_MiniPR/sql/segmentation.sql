-- ==========================================
-- PURCHASE FREQUENCY
-- ==========================================

SELECT

customer_id,

COUNT(order_id) AS TotalOrders,

CASE

WHEN COUNT(order_id)=1

THEN 'One-Time'

WHEN COUNT(order_id)<=5

THEN 'Occasional'

ELSE 'Loyal'

END AS CustomerSegment

FROM orders

GROUP BY customer_id

ORDER BY TotalOrders DESC;

-- ==========================================
-- SPEND TIER
-- ==========================================

SELECT

c.customer_id,

c.customer_name,

ROUND(

SUM(

oi.quantity*
oi.unit_price*
(1-discount_percent/100.0)

),2)

AS TotalSpend,

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

GROUP BY

c.customer_id,
c.customer_name

ORDER BY TotalSpend DESC;

-- ==========================================
-- RECENCY
-- ==========================================

SELECT

customer_id,

MAX(order_date)

AS LastPurchase,

julianday('now')-

julianday(MAX(order_date))

AS DaysSinceLastPurchase

FROM orders

GROUP BY customer_id;

-- ==========================================
-- FREQUENCY
-- ==========================================

SELECT

customer_id,

COUNT(order_id)

AS Frequency

FROM orders

GROUP BY customer_id;

-- ==========================================
-- MONETARY
-- ==========================================

SELECT

o.customer_id,

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

GROUP BY o.customer_id;

-- ==========================================
-- COMPLETE RFM
-- ==========================================

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

FROM RFM

ORDER BY Monetary DESC;

-- ==========================================
-- CUSTOMER CATEGORY
-- ==========================================

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

Monetary,

CASE

WHEN

Frequency>=5

AND Monetary>150000

THEN 'Champion'

WHEN

Frequency>=3

THEN 'Loyal'

WHEN

Frequency=2

THEN 'Potential'

ELSE

'At Risk'

END

AS Segment

FROM RFM

ORDER BY Monetary DESC;

