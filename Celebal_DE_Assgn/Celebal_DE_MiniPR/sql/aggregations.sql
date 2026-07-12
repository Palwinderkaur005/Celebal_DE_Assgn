-- ============================================
-- QUERY 1 : Total Revenue
-- ============================================

SELECT
ROUND(
SUM(
quantity * unit_price *
(1-discount_percent/100.0)
),2) AS Total_Revenue
FROM order_items;

-- ============================================
-- QUERY 2 : Revenue Per Customer
-- ============================================

SELECT

c.customer_id,
c.customer_name,

ROUND(
SUM(
oi.quantity *
oi.unit_price *
(1-oi.discount_percent/100.0)
),2) AS Revenue

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

JOIN order_items oi
ON o.order_id=oi.order_id

GROUP BY
c.customer_id,
c.customer_name

ORDER BY Revenue DESC;

-- ============================================
-- QUERY 3 : Revenue Per Category
-- ============================================

SELECT

p.category,

ROUND(
SUM(
oi.quantity *
oi.unit_price *
(1-oi.discount_percent/100.0)
),2) AS Revenue

FROM products p

JOIN order_items oi

ON p.product_id=oi.product_id

GROUP BY p.category

ORDER BY Revenue DESC;

-- ============================================
-- QUERY 4 : Monthly Revenue
-- ============================================

SELECT

strftime('%Y-%m',o.order_date) AS Month,

ROUND(
SUM(
oi.quantity *
oi.unit_price *
(1-discount_percent/100.0)
),2) AS Revenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

GROUP BY Month

ORDER BY Month;

-- ============================================
-- QUERY 5 : Top 10 Products
-- ============================================

SELECT

p.product_name,

SUM(oi.quantity) AS Quantity

FROM products p

JOIN order_items oi

ON p.product_id=oi.product_id

GROUP BY p.product_name

ORDER BY Quantity DESC

LIMIT 10;

-- ============================================
-- QUERY 6 : Average Order Value
-- ============================================

SELECT

ROUND(
AVG(OrderTotal),2
) AS Average_Order_Value

FROM
(
SELECT

order_id,

SUM(
quantity*
unit_price*
(1-discount_percent/100.0)
) AS OrderTotal

FROM order_items

GROUP BY order_id
);

-- ============================================
-- QUERY 7 : Orders Per Region
-- ============================================

SELECT

region,

COUNT(*) AS Orders

FROM orders

GROUP BY region;

-- ============================================
-- QUERY 8 : Customer Count By Type
-- ============================================

SELECT

customer_type,

COUNT(*) AS Customers

FROM customers

GROUP BY customer_type;