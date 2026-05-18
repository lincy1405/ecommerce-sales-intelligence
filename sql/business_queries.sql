
-- ═══════════════════════════════════════════════════════════
-- E-Commerce Sales Intelligence — Business Queries
-- Dataset: UK Online Retail II (2009-2011)
-- Author: Lincy DCosta
-- ═══════════════════════════════════════════════════════════

-- Q1: Which are the top 10 countries by revenue? (excl. UK)
-- Business Question: Where should we focus international expansion?
SELECT 
    Country,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    COUNT(DISTINCT Invoice) AS Total_Orders,
    ROUND(SUM(Revenue) / COUNT(DISTINCT Invoice), 2) AS Avg_Order_Value
FROM retail
WHERE Country != 'United Kingdom'
GROUP BY Country
ORDER BY Total_Revenue DESC
LIMIT 10;

-- Q2: Top 10 best selling products by revenue
-- Business Question: Which products drive the most value?
SELECT 
    Description,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    SUM(Quantity) AS Total_Quantity,
    COUNT(DISTINCT Invoice) AS Times_Ordered
FROM retail
GROUP BY Description
ORDER BY Total_Revenue DESC
LIMIT 10;

-- Q3: Monthly revenue trend
-- Business Question: When are our peak and low seasons?
SELECT 
    SUBSTR(InvoiceDate, 1, 7) AS Month,
    ROUND(SUM(Revenue), 2) AS Monthly_Revenue,
    COUNT(DISTINCT Invoice) AS Orders,
    COUNT(DISTINCT "Customer ID") AS Unique_Customers
FROM retail
GROUP BY Month
ORDER BY Month;

-- Q4: Key business KPIs
-- Business Question: What are our overall performance metrics?
SELECT 
    ROUND(SUM(Revenue) / COUNT(DISTINCT Invoice), 2) AS Overall_AOV,
    ROUND(AVG(Revenue), 2) AS Avg_Item_Revenue,
    COUNT(DISTINCT "Customer ID") AS Total_Customers,
    COUNT(DISTINCT Invoice) AS Total_Orders
FROM retail;

-- Q5: Top 10 customers by lifetime value
-- Business Question: Who are our most valuable customers to retain?
SELECT 
    "Customer ID",
    Country,
    COUNT(DISTINCT Invoice) AS Total_Orders,
    ROUND(SUM(Revenue), 2) AS Total_Spent,
    ROUND(SUM(Revenue) / COUNT(DISTINCT Invoice), 2) AS Avg_Order_Value
FROM retail
WHERE "Customer ID" IS NOT NULL
GROUP BY "Customer ID"
ORDER BY Total_Spent DESC
LIMIT 10;

-- Q6: RFM Base Table — Recency, Frequency, Monetary
-- Business Question: How do we segment customers by engagement?
SELECT 
    "Customer ID",
    Country,
    MAX(SUBSTR(InvoiceDate, 1, 10)) AS Last_Purchase_Date,
    COUNT(DISTINCT Invoice) AS Frequency,
    ROUND(SUM(Revenue), 2) AS Monetary
FROM retail
WHERE "Customer ID" IS NOT NULL
GROUP BY "Customer ID"
ORDER BY Monetary DESC
LIMIT 15;
