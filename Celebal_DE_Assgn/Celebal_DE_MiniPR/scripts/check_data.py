import pandas as pd

df = pd.read_csv("data/raw/customers.csv")

print("\nFirst 5 rows")
print(df.head())

print("\nInformation")
print(df.info())

print("\nDescription")
print(df.describe(include="all"))