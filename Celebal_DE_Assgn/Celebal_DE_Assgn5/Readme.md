# Apache Spark Data Cleaning and Aggregation using DataFrames

## Objective

The objective of this assignment is to understand Apache Spark fundamentals and perform data cleaning, transformation, filtering, and aggregation operations using Spark DataFrames.

---

## Topics Covered

* Introduction to Apache Spark
* Limitations of MapReduce
* In-Memory Computing in Spark
* Spark DataFrames
* Data Cleaning
* Handling Missing Values
* Filtering Data
* Schema Modification
* Aggregation Functions
* GroupBy Operations
* Shuffle and Wide Transformations
* Complete Data Processing Pipeline

---

## Technologies Used

* Python
* PySpark
* Google Colab 
* Pandas

---

## Project Structure

```
Celebal_DE_Assgn5/
│
├── data/
│   └── dataset.csv
│
├── notebook/
│   └── spark_basics.ipynb
│
├── output/
│   └── results.csv
│── Week5 Assgn QNA
└── README.md
```

---

## Dataset

The dataset contains information about users, transactions, product categories, sales amount, prices, store IDs, timestamps, and other attributes. It also includes duplicate records and missing values to demonstrate data cleaning operations.

---

## Operations Performed

### Data Loading

* Loaded CSV data into Spark DataFrame.
* Displayed schema and sample records.

### Data Cleaning

* Removed duplicate records.
* Handled missing values.
* Removed invalid records.
* Managed inconsistent data.

### Filtering

* Applied conditions on:

  * Age
  * Subscription type
  * Region

### Transformations

* Renamed columns.
* Cast data types.
* Converted timestamps.

### Aggregation

* Count
* Sum
* Average
* Minimum
* Maximum

### Grouping Operations

* Grouped records using `groupBy()`.
* Applied aggregate functions.

### Final Processing Pipeline

* Removed duplicates.
* Filled null prices with zero.
* Calculated total revenue for each store.

---

## Output

The final processed results are stored in:

```
output/results.csv
```

---

## Learning Outcomes

After completing this assignment, I was able to:

* Understand Spark architecture and advantages over MapReduce.
* Work with Spark DataFrames.
* Perform data cleaning and preprocessing.
* Apply filtering and aggregation operations.
* Understand shuffle and wide transformations.
* Build an end-to-end data processing pipeline using PySpark.
