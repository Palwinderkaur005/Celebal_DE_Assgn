CREATE DATABASE SuperstoreDB;
USE SuperstoreDB;
SELECT * FROM superstore LIMIT 10;
SELECT COUNT(*) FROM superstore;
DESCRIBE superstore;
SELECT *
FROM superstore
WHERE Region='West';
SELECT *
FROM superstore
WHERE Category='Technology';
SELECT *
FROM superstore
WHERE Sales > 1000;
SELECT *
FROM superstore
WHERE `Order Date` LIKE '%2016%';
SELECT SUM(Sales) AS Total_Sales
FROM superstore;
SELECT SUM(Quantity) AS Total_Quantity
FROM superstore;
SELECT AVG(Sales) AS Average_Sales
FROM superstore;
SELECT MAX(Sales) AS Highest_Sale
FROM superstore;
SELECT MIN(Sales) AS Lowest_Sale
FROM superstore;
SELECT `Product Name`,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT Category,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC
LIMIT 5;
SELECT `Customer Name`,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT `Product Name`,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Profit DESC;
SELECT DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m')
ORDER BY Month;
SELECT DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m')
ORDER BY Month;
SELECT `Customer Name`,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT `Customer Name`,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Profit DESC
LIMIT 10;
SELECT `Order ID`,
       COUNT(*) AS Occurrences
FROM superstore
GROUP BY `Order ID`
HAVING COUNT(*) > 1;
SELECT COUNT(*) AS Duplicate_Orders
FROM (
    SELECT `Order ID`
    FROM superstore
    GROUP BY `Order ID`
    HAVING COUNT(*) > 1
) AS duplicates;
SELECT Region,
       `Customer Name`,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region, `Customer Name`
ORDER BY Region, Total_Sales DESC;
SELECT COUNT(*) AS Total_Rows
FROM superstore;
DESCRIBE superstore;
SELECT COUNT(*) AS Missing_Customers
FROM superstore
WHERE `Customer Name` IS NULL;
SELECT COUNT(*) AS Missing_Products
FROM superstore
WHERE `Product Name` IS NULL;
SELECT COUNT(*) AS Missing_Sales
FROM superstore
WHERE Sales IS NULL;
SELECT *
FROM superstore
WHERE Profit < 0;
SELECT COUNT(DISTINCT `Customer Name`) AS Total_Customers
FROM superstore;
SELECT COUNT(DISTINCT `Product Name`) AS Total_Products
FROM superstore;