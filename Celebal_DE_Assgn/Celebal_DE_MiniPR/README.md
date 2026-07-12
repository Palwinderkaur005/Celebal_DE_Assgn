# 🛒 E-Commerce Order Analytics System

## 📌 Project Overview

The **E-Commerce Order Analytics System** is an end-to-end data analytics project built using **Python, Pandas, SQLite, and SQL**. The system generates realistic e-commerce datasets, performs data cleaning and validation, loads the cleaned data into a relational database, executes advanced SQL analytics, and provides a command-line interface (CLI) for generating business reports.

The project demonstrates the complete data analytics pipeline, from raw data generation to business insights.

---

# 🎯 Objectives

- Generate realistic e-commerce datasets using Python.
- Introduce intentional inconsistencies for data cleaning practice.
- Clean and validate datasets using Pandas.
- Maintain referential integrity across multiple tables.
- Load cleaned data into SQLite.
- Perform advanced SQL analytics.
- Implement Window Functions and Common Table Expressions (CTEs).
- Conduct Cohort Analysis and Customer Segmentation (RFM).
- Build a CLI-based reporting tool.
- Handle edge cases and invalid inputs gracefully.

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Programming Language |
| Pandas | Data Cleaning & Processing |
| Faker | Synthetic Data Generation |
| Random | Randomized Dataset Generation |
| SQLite | Relational Database |
| SQL | Data Analytics |
| argparse | CLI Development |
| Tabulate | Formatted CLI Reports |
| VS Code | Development Environment |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```
ecommerce-analytics-system/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   └── order_items.csv
│   │
│   └── cleaned/
│       ├── customers_clean.csv
│       ├── products_clean.csv
│       ├── orders_clean.csv
│       └── order_items_clean.csv
│
├── database/
│   └── ecommerce.db
│
├── scripts/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_database.py
│   ├── database_verify.py
│   ├── test_relationships.py
│   ├── check_customers.py
│   ├── check_products.py
│   ├── check_orders.py
│   ├── check_order_items.py
│   ├── check_cleaned_data.py
│   ├── run_queries.py
│   ├── run_window_queries.py
│   ├── run_cohort_queries.py
│   ├── run_segmentation.py
│   └── report_cli.py
│
├── sql/
│   ├── schema.sql
│   ├── aggregations.sql
│   ├── window_functions.sql
│   ├── cohort_analysis.sql
│   └── segmentation.sql
│
├── output/
│   └── sample_reports/
│
└── README.md
```

---

# 📊 Dataset Generation

The following datasets were generated using the **Faker** library and Python's **random** module.

### Customers

Contains:

- Customer ID
- Customer Name
- Email
- Registration Date
- Customer Type

Intentional inconsistencies:

- Invalid Emails
- Duplicate Records
- Missing Values

---

### Products

Contains:

- Product ID
- Product Name
- Category
- Subcategory
- Cost Price

Intentional inconsistencies:

- Duplicate Products
- Null Categories

---

### Orders

Contains:

- Order ID
- Customer ID
- Order Date
- Region
- Status

Intentional inconsistencies:

- Future Dates
- Missing Customer IDs
- Invalid Customer IDs

---

### Order Items

Contains:

- Item ID
- Order ID
- Product ID
- Quantity
- Unit Price
- Discount Percentage

Intentional inconsistencies:

- Invalid Order IDs
- Invalid Product IDs
- Negative Quantities
- Discount >100%

---

# 🧹 Data Cleaning

Performed using **Pandas**.

Cleaning operations include:

- Removing duplicates
- Handling missing values
- Removing invalid emails
- Standardizing text
- Removing future dates
- Removing invalid quantities
- Removing invalid discounts
- Referential Integrity Validation
- Exporting cleaned datasets

---

# 🗄 Database Design

SQLite database contains four tables.

## Customers

Primary Key:

- customer_id

---

## Products

Primary Key:

- product_id

---

## Orders

Primary Key:

- order_id

Foreign Key:

- customer_id

---

## Order Items

Primary Key:

- item_id

Foreign Keys:

- order_id
- product_id

---

# 📈 SQL Analytics

Implemented SQL operations include:

### Joins

- Customer Revenue
- Category Revenue
- Product Revenue

### Aggregations

- Total Revenue
- Monthly Revenue
- Revenue by Category
- Revenue by Customer
- Orders by Region
- Average Order Value

---

# 📊 Window Functions

Implemented:

- RANK()
- DENSE_RANK()
- SUM() OVER()
- AVG() OVER()
- Running Totals
- Moving Average

---

# 📑 Common Table Expressions (CTEs)

Implemented:

- Monthly Revenue Growth
- Customer Lifetime Value
- Multi-step Revenue Calculations

---

# 👥 Cohort Analysis

Implemented:

- First Purchase Month
- Monthly Customer Retention
- Repeat Customers
- One-Time Customers
- Churned Customers

---

# 🎯 Customer Segmentation

Implemented:

### Purchase Frequency

- One-Time
- Occasional
- Loyal

### Spend Tier

- Low
- Medium
- High

### RFM Analysis

Calculated:

- Recency
- Frequency
- Monetary Value

Generated customer segments:

- Champion
- Loyal
- Potential
- At Risk

---

# 💻 Command Line Reporting Tool

Supported reports:

```bash
python scripts/report_cli.py --report revenue

python scripts/report_cli.py --report top_customers

python scripts/report_cli.py --report retention

python scripts/report_cli.py --report rfm
```

---

# ⚠ Edge Case Handling

The system handles:

- Empty datasets
- Invalid CLI inputs
- Missing database
- Invalid customer IDs
- Invalid order IDs
- Future dates
- Duplicate rows
- Null values

---

# ▶ How to Run

## Install Dependencies

```bash
pip install pandas faker tabulate
```

---

## Generate Dataset

```bash
python scripts/generate_data.py
```

---

## Clean Dataset

```bash
python scripts/clean_data.py
```

---

## Load Database

```bash
python scripts/load_database.py
```

---

## Verify Database

```bash
python scripts/database_verify.py
```

---

## Execute Aggregation Queries

```bash
python scripts/run_queries.py
```

---

## Execute Window Function Queries

```bash
python scripts/run_window_queries.py
```

---

## Execute Cohort Analysis

```bash
python scripts/run_cohort_queries.py
```

---

## Execute Customer Segmentation

```bash
python scripts/run_segmentation.py
```

---

## Generate Reports

Revenue Report

```bash
python scripts/report_cli.py --report revenue
```

Top Customers

```bash
python scripts/report_cli.py --report top_customers
```

Retention Report

```bash
python scripts/report_cli.py --report retention
```

RFM Report

```bash
python scripts/report_cli.py --report rfm
```

---

# 📸 Sample Output

Include screenshots of:

- Project Folder Structure
- Generated Raw CSV Files
- Cleaned CSV Files
- SQLite Database Tables
- SQL Query Results
- Window Function Output
- Cohort Analysis Output
- Customer Segmentation Output
- CLI Revenue Report
- CLI Top Customers Report
- CLI Retention Report
- CLI RFM Report

---

# 🚀 Future Improvements

- Interactive Dashboard using Power BI or Tableau
- Web Application using Streamlit
- MySQL/PostgreSQL Support
- Automated ETL Pipeline
- Scheduled Report Generation
- Data Visualization
- Docker Containerization

---

# 👨‍💻 Author

**Palwinder Kaur**

B.Tech Computer Science & Engineering

Maharishi Markandeshwar (Deemed to be University), Mullana

---

# ⭐ Learning Outcomes

This project demonstrates:

- Python Programming
- Data Cleaning using Pandas
- SQL Database Design
- SQL Joins
- SQL Aggregations
- Window Functions
- CTEs
- Cohort Analysis
- Customer Segmentation
- CLI Application Development
- End-to-End Data Analytics Pipeline