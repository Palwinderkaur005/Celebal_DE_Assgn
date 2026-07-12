import pandas as pd

df = pd.read_csv("data/raw/order_items.csv")

print("="*60)
print("ORDER ITEMS DATASET")
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