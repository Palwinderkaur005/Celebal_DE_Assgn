import pandas as pd

df = pd.read_csv("data/raw/products.csv")

print("="*60)
print("PRODUCTS DATASET")
print("="*60)

print(df.head())

print("\nInfo")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicates")
print(df.duplicated().sum())

print("\nSummary")
print(df.describe(include="all"))