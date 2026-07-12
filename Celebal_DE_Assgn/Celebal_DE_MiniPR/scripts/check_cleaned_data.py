import pandas as pd

files = {
    "Customers": "data/cleaned/customers_clean.csv",
    "Products": "data/cleaned/products_clean.csv",
    "Orders": "data/cleaned/orders_clean.csv",
    "Order Items": "data/cleaned/order_items_clean.csv"
}

for name, path in files.items():
    print("=" * 60)
    print(name)
    print("=" * 60)

    df = pd.read_csv(path)

    print("Rows:", len(df))
    print("Columns:", list(df.columns))
    print("Missing Values")
    print(df.isnull().sum())
    print()