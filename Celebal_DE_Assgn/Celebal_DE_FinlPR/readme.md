# Startup Funding Analysis using Medallion Architecture

## 📌 Project Overview

This project demonstrates an end-to-end data engineering pipeline using the **Medallion Architecture (Bronze → Silver → Gold)** on the **Indian Startup Funding** dataset. The pipeline ingests raw CSV data, cleans and standardizes it using **PySpark**, stores each processing stage as **Delta Tables**, and generates business insights using **SQL**.

The project is implemented in **Databricks Free Edition** using **Apache Spark**, **Delta Lake**, and **Unity Catalog Volumes**.

---

## 🏗️ Medallion Architecture

```
                     Startup Funding CSV
                              │
                              ▼
                     Bronze Layer (Raw Data)
                              │
                              ▼
              Silver Layer (Cleaned & Standardized)
                              │
                              ▼
               Gold Layer (Business Aggregations)
          ┌──────────────┬──────────────┬──────────────┐
          ▼              ▼              ▼
   Top Industries   City Ranking   Investor Activity
                              │
                              ▼
                       SQL Analytics
```

---

## 🎯 Objectives

- Ingest raw CSV data into Databricks.
- Build Bronze, Silver, and Gold layers using Delta Lake.
- Perform data cleaning and standardization using PySpark.
- Generate business insights using SQL.
- Demonstrate an end-to-end modern data engineering workflow.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Databricks Free Edition | Development Environment |
| Apache Spark | Distributed Data Processing |
| PySpark | Data Transformation |
| Delta Lake | Data Storage |
| SQL | Business Analytics |
| Unity Catalog | Data Management |

---

## 📂 Repository Structure

```
Startup-Funding-Medallion-Architecture/
│
├── README.md
│
├── data/
│   └── startup_funding.csv
│
├── notebooks/
│   ├── Bronze_Layer.ipynb
│   ├── Silver_Layer.ipynb
│   ├── Gold_Layer.ipynb
│   └── SQL_Analysis.ipynb
│
├── sql/
│   ├── top_industries.sql
│   ├── city_ranking.sql
│   ├── investor_activity.sql
│   └── investment_type_analysis.sql
│
├── screenshots/
│   ├── csv_upload.png
│   ├── raw_data.png
│   ├── bronze_layer.png
│   ├── silver_layer.png
│   ├── gold_top_industries.png
│   ├── city_ranking.png
│   ├── investor_activity.png
│
└── docs/
    └── architecture.png
```

---

# 📊 Dataset

Dataset Used:

**Indian Startup Funding Dataset**

### Dataset Columns

- Startup
- Industry
- SubVertical
- City
- Investors
- InvestmentType
- InvestmentAmount_USD
- Date

---

# 🚀 Workflow

## Step 1: Bronze Layer

### Purpose

The Bronze layer stores the raw data exactly as received without applying any transformations.

### Operations Performed

- Upload CSV into Unity Catalog Volume
- Read CSV using PySpark
- Infer schema
- Store as Delta Table

Output:

```
Raw Delta Table
```

---

## Step 2: Silver Layer

### Purpose

The Silver layer contains cleaned and standardized data ready for analysis.

### Transformations Performed

- Removed duplicate records
- Removed completely null rows
- Cleaned InvestmentAmount_USD
- Converted InvestmentAmount_USD to numeric type
- Standardized text columns
- Standardized date format

Output:

```
Clean Delta Table
```

---

## Step 3: Gold Layer

### Purpose

The Gold layer contains aggregated business-ready datasets.

### Aggregations Created

- Top Industries by Investment
- City-wise Investment Ranking
- Most Active Investors
- Investment Type Analysis

Output:

```
Business Analytics Tables
```

---

# 📈 SQL Analysis

The following SQL queries were performed:

### Top Industries

```sql
SELECT Industry,
SUM(InvestmentAmount_USD) AS Total_Investment
FROM silver_startup
GROUP BY Industry
ORDER BY Total_Investment DESC;
```

---

### City Ranking

```sql
SELECT City,
SUM(InvestmentAmount_USD) AS Total_Investment
FROM silver_startup
GROUP BY City
ORDER BY Total_Investment DESC;
```

---

### Investor Activity

```sql
SELECT Investors,
COUNT(*) AS Deals
FROM silver_startup
GROUP BY Investors
ORDER BY Deals DESC;
```

---

### Investment Type Analysis

```sql
SELECT InvestmentType,
COUNT(*) AS Number_of_Deals,
SUM(InvestmentAmount_USD) AS Total_Investment
FROM silver_startup
GROUP BY InvestmentType
ORDER BY Total_Investment DESC;
```

---

# 📊 Key Insights

The pipeline generates valuable business insights such as:

- Top funded industries
- Cities receiving maximum investments
- Most active investors
- Distribution of investment types
- Overall investment trends

---

# 📷 Project Screenshots

The repository contains screenshots for every major stage of the pipeline.

| Screenshot | Description |
|------------|-------------|
| csv_upload.png | CSV uploaded to Unity Catalog Volume |
| raw_data.png | Raw dataset preview |
| bronze_layer.png | Bronze Delta Layer |
| silver_layer.png | Cleaned Silver Layer |
| gold_top_industries.png | Top Industries Analysis |
| city_ranking.png | City-wise Investment Ranking |
| investor_activity.png | Most Active Investors |

---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone 
```

### 2. Open Databricks

Create a notebook and attach **Serverless Compute**.

### 3. Upload Dataset

Upload `startup_funding.csv` into the Unity Catalog Volume.
Dataset: https://www.kaggle.com/datasets/vagdevititikshag/indian-startup-funding-dataset-20202025


### 4. Execute Notebooks

Run the notebooks in the following order:

1. Bronze_Layer.ipynb
2. Silver_Layer.ipynb
3. Gold_Layer.ipynb
4. SQL_Analysis.ipynb

---

# 📌 Results

✔ Successfully implemented the Medallion Architecture.

✔ Built Bronze, Silver, and Gold Delta layers.

✔ Cleaned and standardized startup funding data using PySpark.

✔ Generated business insights using SQL.

✔ Demonstrated a complete modern data engineering pipeline in Databricks.

---

# 📚 Learning Outcomes

Through this project, I learned:

- Medallion Architecture
- Apache Spark Fundamentals
- PySpark Data Cleaning
- Delta Lake
- SQL Analytics
- Unity Catalog
- Databricks Free Edition Workflow

---

## 👤 Author

**Palwinder Kaur**

B.Tech Computer Science & Engineering

Maharishi Markandeshwar (Deemed to be University)

