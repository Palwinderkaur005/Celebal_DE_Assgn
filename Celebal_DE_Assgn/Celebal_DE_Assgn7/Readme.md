# Delta Lake Assignment – Incremental Data Processing


- **Platform:** Databricks Free Edition
- **Technology:** Apache Spark, Delta Lake, PySpark

---

## Objective

Perform incremental data processing using Delta Lake by loading a dataset into a Delta table, cleaning the data, applying incremental updates using the MERGE operation, and validating the final results.

---

## Dataset

The project uses two datasets:

- **customer_master.csv** – Initial customer dataset
- **customer_incremental.csv** – Incremental dataset containing updated and new customer records

---

## Tasks Performed

### 1. Load Master Dataset
- Loaded `customer_master.csv` into a Spark DataFrame.
- Displayed the dataset for verification.

### 2. Data Cleaning
- Identified and handled missing values.
- Removed duplicate records.

### 3. Create Delta Table
- Saved the cleaned master dataset as a Delta table.

### 4. Load Incremental Dataset
- Loaded `customer_incremental.csv`.

### 5. Perform MERGE Operation
- Updated existing customer records.
- Inserted new customer records.
- Used Delta Lake `MERGE` functionality for incremental processing.

### 6. Validate Results
- Verified the total number of records.
- Checked for duplicate records.
- Displayed the final merged dataset.

---

## Technologies Used

- Python
- PySpark
- Apache Spark
- Delta Lake
- Databricks Free Edition

---

## Project Structure

```
delta-lake-assignment/
│
├── data/
│   ├── customer_master.csv
│   └── customer_incremental.csv
│
├── notebooks/
│   └── Delta_Assignment.ipynb
│
├── screenshots/
│   ├── 01_uploaded_files.png
├   |── 02_master_loaded.png
│   ├── 03_cleaning.png
│   ├── 04_delta_table.png
│   ├── 05_incremental_loaded.png
│   ├── 06_merge.png
│   ├── 07_final_data.png
│   ├── 08_row_count.png
│   └── 09_duplicates.png
│
├── report/
│   └── assignment_summary.pdf 
|
└── README.md
```

---

## Screenshots Included

- Master dataset loading
- Data cleaning
- Delta table creation
- Incremental dataset loading
- MERGE operation
- Final merged dataset
- Row count validation
- Duplicate validation

---

## Result

Successfully implemented incremental data processing using Delta Lake. Existing records were updated, new records were inserted through the MERGE operation, and the final dataset was validated with no duplicate records.

---

## Author

**Palwinder Kaur**