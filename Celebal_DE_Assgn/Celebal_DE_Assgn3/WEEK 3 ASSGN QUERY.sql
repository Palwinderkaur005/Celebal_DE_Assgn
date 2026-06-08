-- --Create Databse--
CREATE DATABASE superstore_db;
USE superstore_db;
-- Verify Database
SHOW DATABASES;

-- Create customer table
CREATE TABLE customers AS 
SELECT DISTINCT 
`Customer ID` AS customer_id,
`Customer Name` AS customer_name,
 Segment,
 Country,
 City,
 State,
 Region 
 FROM superstore_raw;
 SELECT *FROM customers;
 
 -- Create products table
 CREATE TABLE products AS 
 SELECT DISTINCT 
 `Product ID` AS product_id,
 Category,
 `Sub-Category` AS sub_category,
 `Product Name` AS product_name 
 FROM superstore_raw;
SELECT *FROM products;

-- CREATE orders table
CREATE TABLE orders AS
 SELECT DISTINCT 
 `Row ID` AS row_id,
 `Order ID` AS order_id,
 `Order Date` AS order_date,
 `Ship Date` AS ship_date,
 `Ship Mode` AS ship_mode,
 `Customer ID` AS customer_id,
 `Product ID` AS product_id,
 Sales,
 Quantity,
 Discount,
 Profit 
 FROM superstore_raw;
 SELECT *FROM orders;
 
 -- Perform Required Queries
SELECT 
 * FROM orders 
 WHERE sales > 
 ( 
   SELECT AVG(sales) 
   FROM orders 
   );
   
-- Highest Sales Order for Each Customer   
SELECT o.customer_id,
       o.order_id,
       o.sales
FROM orders o
JOIN
(
    SELECT customer_id,
           MAX(sales) AS max_sales
    FROM orders
    GROUP BY customer_id
) m
ON o.customer_id = m.customer_id
AND o.sales = m.max_sales;

-- Total Sales for Each Customer
WITH customer_sales AS 
(
 SELECT customer_id,
 SUM(sales) AS total_sales 
 FROM orders GROUP BY customer_id 
 )
 SELECT * FROM customer_sales;
 
 -- Customers with Above-Average Total Sales
 WITH customer_sales AS ( SELECT customer_id, SUM(sales) AS total_sales FROM orders GROUP BY customer_id ) SELECT * FROM customer_sales WHERE total_sales > ( SELECT AVG(total_sales) FROM customer_sales );
 
 -- Rank Customers Based on Total Sales
WITH customer_sales AS
(
    SELECT customer_id,
           SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT customer_id,
       total_sales,
       RANK() OVER(ORDER BY total_sales DESC) AS sales_rank
FROM customer_sales;

-- Assign Row Numbers to Orders Within Each Customer
SELECT customer_id,
       order_id,
       sales,
       ROW_NUMBER() OVER
       (
           PARTITION BY customer_id
           ORDER BY sales DESC
       ) AS row_num
FROM orders;

-- Top 3 Customers Based on Total Sales
WITH customer_sales AS
(
    SELECT customer_id,
           SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT *
FROM
(
    SELECT customer_id,
           total_sales,
           RANK() OVER(ORDER BY total_sales DESC) AS sales_rank
    FROM customer_sales
) ranked_customers
WHERE sales_rank <= 3;


-- Final Combined Query
WITH customer_sales AS
(
    SELECT c.customer_id,
           c.customer_name,
           SUM(o.sales) AS total_sales
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_id,
             c.customer_name
)

SELECT customer_name,
       total_sales,
       RANK() OVER(ORDER BY total_sales DESC) AS sales_rank
FROM customer_sales;


-- MINI PROJECT 
-- TOP 5 COMPANIES
WITH customer_sales AS
(
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(o.sales) AS total_sales
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name
)

SELECT *
FROM customer_sales
ORDER BY total_sales DESC
LIMIT 5;

-- BOTTOM 5 COMPANIES
WITH customer_sales AS
(
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(o.sales) AS total_sales
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name
)

SELECT *
FROM customer_sales
ORDER BY total_sales ASC
LIMIT 5;

-- Customers Made Only One Order
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(DISTINCT o.order_id) = 1;

-- Customers Have Above-Average Sales
WITH customer_sales AS
(
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(o.sales) AS total_sales
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name
)

SELECT *
FROM customer_sales
WHERE total_sales >
(
    SELECT AVG(total_sales)
    FROM customer_sales
);

-- Highest Order Value Per Customer
SELECT
    c.customer_id,
    c.customer_name,
    MAX(o.sales) AS highest_order_value
FROM customers c
JOIN orders o
GROUP BY c.customer_id, c.customer_name
ORDER BY highest_order_value DESC;