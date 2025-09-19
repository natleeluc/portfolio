CREATE DATABASE crm_project; 
USE crm_project;

CREATE TABLE customers (
  ID INT,
  Year_Birth INT,
  Education VARCHAR(50),
  Marital_Status VARCHAR(50),
  Income FLOAT,
  Kidhome INT,
  Teenhome INT,
  Dt_Customer DATE,
  Recency INT,
  MntWines INT,
  MntFruits INT,
  MntMeatProducts INT,
  MntFishProducts INT,
  MntSweetProducts INT,
  MntGoldProds INT,
  NumDealsPurchases INT,
  NumWebPurchases INT,
  NumCatalogPurchases INT,
  NumStorePurchases INT,
  NumWebVisitsMonth INT,
  AcceptedCmp1 INT,
  AcceptedCmp2 INT,
  AcceptedCmp3 INT,
  AcceptedCmp4 INT,
  AcceptedCmp5 INT,
  Response INT,
  Complain INT,
  Country VARCHAR(50)
);


-- Vliv kampaní na chování zákazníků
SELECT
  ID,
  (AcceptedCmp1 + AcceptedCmp2 + AcceptedCmp3 + AcceptedCmp4 + AcceptedCmp5) AS Campaigns_Accepted,
  (MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds) AS Total_Spend
FROM marketing_clean;


-- Délka členství vs. útrata
SELECT
id, 
  DATEDIFF(CURDATE(), STR_TO_DATE(Dt_Customer, '%d.%m.%Y')) / 365 AS Years_As_Customer,
  (MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds) AS Total_Spend
FROM marketing_clean;


-- Kompletní dotaz: RFM + skóre + segment 

SELECT
  ID,
  Recency,
  Frequency,
  Monetary,

  CASE 
    WHEN Recency <= 30 THEN 4
    WHEN Recency <= 60 THEN 3
    WHEN Recency <= 90 THEN 2
    ELSE 1
  END AS R_Score,

  CASE 
    WHEN Frequency >= 10 THEN 4
    WHEN Frequency >= 6 THEN 3
    WHEN Frequency >= 3 THEN 2
    ELSE 1
  END AS F_Score,

  CASE 
    WHEN Monetary >= 1000 THEN 4
    WHEN Monetary >= 500 THEN 3
    WHEN Monetary >= 200 THEN 2
    ELSE 1
  END AS M_Score,

  -- Segment podle RFM skóre 
  CASE
    WHEN Recency <= 30 AND Frequency >= 10 AND Monetary >= 1000 THEN 'Champions'
    WHEN Recency <= 60 AND Frequency >= 6 THEN 'Loyal Customers'
    WHEN Recency > 90 AND Frequency >= 5 THEN 'At Risk'
    WHEN Recency <= 30 AND Frequency <= 3 THEN 'New Customers'
    ELSE 'Others'
  END AS Segment

FROM (
  SELECT
    ID,
    Recency,
    NumStorePurchases + NumWebPurchases + NumCatalogPurchases AS Frequency,
    (MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds) AS Monetary
  FROM marketing_clean
) AS base;

-- Zákaznické fáze podle recency (životní cyklus) 
SELECT 
  ID,
  Recency,
  CASE 
    WHEN Recency <= 30 THEN 'Aktivní'
    WHEN Recency <= 90 THEN 'Středně aktivní'
    ELSE 'Neaktivní'
  END AS Activity_Segment
FROM marketing_clean;
