# Week-6: Spark Data Processing Assignment

## Overview

This project demonstrates the fundamentals of Apache Spark using PySpark. It covers Spark architecture, lazy evaluation, DataFrame transformations, schema handling, filtering, optimized file formats, and building a complete data processing pipeline. The assignment also compares CSV and Parquet file formats and explores Spark performance optimization techniques.

---

## Objective

The objective of this assignment is to:

* Understand Spark Architecture (Driver, Cluster Manager, Executors)
* Learn Lazy Evaluation and DAG (Lineage Graph)
* Read and process CSV and Parquet files
* Perform DataFrame transformations and filtering
* Handle schemas and data types
* Manage null values efficiently
* Understand Predicate Pushdown and Shuffle operations
* Build a complete Spark data processing pipeline
* Save processed data in CSV and Parquet formats
* Follow Spark best practices for handling large datasets

---

## Technologies Used

* Python 3
* Apache Spark (PySpark)
* Google Colab
* Pandas
* Java (OpenJDK)

---

## Repository Structure

```
Week6-Spark-Assignment/
│
├── notebook/
│   └── Week6_Spark_Assignment.ipynb
│
├── data/
│   └── source.csv
│
├── screenshots/
│  
│
├── README.md

```

---

## Assignment Tasks

The following tasks were performed during the assignment:

* Created a Spark Session
* Understood Spark Architecture
* Explained Driver, Cluster Manager and Executors
* Demonstrated Lazy Evaluation
* Explored DAG (Lineage Graph)
* Read CSV files with schema inference
* Selected required columns
* Filtered records using conditions
* Renamed DataFrame columns
* Cast data types
* Added computed columns
* Handled null values
* Compared CSV and Parquet formats
* Demonstrated Predicate Pushdown
* Built a complete ETL pipeline
* Saved processed data into CSV and Parquet
* Explained Spark Transformations and Actions

---

## Spark Data Processing Pipeline

```
Read CSV
     │
     ▼
Infer Schema
     │
     ▼
Filter Records
     │
     ▼
Rename Columns
     │
     ▼
Cast Data Types
     │
     ▼
Handle Null Values
     │
     ▼
Add New Columns
     │
     ▼
Select Required Columns
     │
     ▼
Write CSV
     │
     ▼
Write Parquet
```

---

## Key Spark Concepts Covered

### Spark Architecture

* Driver Program
* Cluster Manager
* Executors
* Tasks

### DataFrame Operations

* Read CSV
* Read Parquet
* Select
* Filter
* Rename Columns
* Cast Data Types
* Add New Columns

### Performance Concepts

* Lazy Evaluation
* DAG (Lineage Graph)
* Predicate Pushdown
* Shuffle
* Wide Transformations

### File Formats

* CSV
* Parquet

---

## CSV vs Parquet

| Feature            | CSV       | Parquet  |
| ------------------ | --------- | -------- |
| Storage            | Row-Based | Columnar |
| Compression        | No        | Yes      |
| File Size          | Large     | Smaller  |
| Performance        | Slower    | Faster   |
| Predicate Pushdown | No        | Yes      |

---

## Best Practices Followed

* Used `show()` instead of `collect()` for data preview.
* Applied filtering before expensive transformations.
* Selected only required columns.
* Used schema inference for structured data.
* Stored processed data in Parquet format for better performance.
* Avoided unnecessary data loading into memory.

---

## Learning Outcomes

After completing this assignment, I learned:

* Spark Architecture and execution flow
* Difference between Transformations and Actions
* Importance of Lazy Evaluation
* Working with Spark DataFrames
* Reading and writing CSV and Parquet files
* Data filtering and schema handling
* Performance optimization using Predicate Pushdown
* Building scalable ETL pipelines using PySpark

---

## Conclusion

This assignment provided practical experience with Apache Spark and PySpark for distributed data processing. It demonstrated how Spark optimizes execution using Lazy Evaluation and DAG, how DataFrames can be transformed efficiently, and why Parquet is preferred over CSV for analytical workloads. The assignment also highlighted best practices for handling large datasets and building efficient data processing pipelines.
