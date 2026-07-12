-- ===========================================
-- Query 1 : Customer Lifetime Value Ranking
-- ===========================================

SELECT
    c.customer_id,
    c.customer_name,

    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount_percent / 100.0)
        ),2
    ) AS Lifetime_Value,

    RANK() OVER(
        ORDER BY
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount_percent / 100.0)
        ) DESC
    ) AS Customer_Rank

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY
c.customer_id,
c.customer_name;

-- ===========================================
-- Query 2 : Dense Rank
-- ===========================================

SELECT

c.customer_name,

ROUND(

SUM(
oi.quantity *
oi.unit_price *
(1-discount_percent/100.0)

),2)

AS Revenue,

DENSE_RANK()

OVER(

ORDER BY

SUM(

oi.quantity *
oi.unit_price *
(1-discount_percent/100.0)

) DESC

)

AS Dense_Rank

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY c.customer_name;

-- ===========================================
-- Query 3 : Running Total
-- ===========================================

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

strftime('%Y-%m',o.order_date)

AS Month,

ROUND(

SUM(

oi.quantity*

oi.unit_price*

(1-discount_percent/100.0)

),2)

AS Revenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY Month

);

-- ===========================================
-- Query 4 : Moving Average
-- ===========================================

SELECT

Month,

Revenue,

ROUND(

AVG(Revenue)

OVER(

ORDER BY Month

ROWS BETWEEN 2 PRECEDING

AND CURRENT ROW

),2)

AS Moving_Average

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

-- ===========================================
-- Query 5 : CTE
-- Monthly Revenue Growth
-- ===========================================

WITH MonthlyRevenue AS (

SELECT

strftime('%Y-%m',o.order_date)

AS Month,

SUM(

oi.quantity*

oi.unit_price*

(1-discount_percent/100.0)

)

AS Revenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY Month

)

SELECT

Month,

ROUND(Revenue,2)

AS Revenue,

ROUND(

Revenue

-

LAG(Revenue)

OVER(

ORDER BY Month

),2)

AS Growth

FROM MonthlyRevenue;

