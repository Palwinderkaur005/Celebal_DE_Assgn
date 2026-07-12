import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")

# -------------------------------
# CREATE FOLDERS
# -------------------------------
import os

os.makedirs("data/raw", exist_ok=True)

# =====================================================
# CUSTOMERS DATASET
# =====================================================

NUM_CUSTOMERS = 500

customers = []

customer_types = [
    "REGULAR",
    "PREMIUM",
    "VIP"
]

for i in range(NUM_CUSTOMERS):

    customer_id = f"C{i+1:04d}"

    customer_name = fake.name()

    email = fake.email()

    registration_date = fake.date_between(
        start_date="-3y",
        end_date="today"
    )

    customer_type = random.choice(customer_types)

    # Introduce 2% invalid emails
    if random.random() < 0.02:
        email = email.replace("@", "")

    customers.append({
        "customer_id": customer_id,
        "customer_name": customer_name,
        "email": email,
        "registration_date": registration_date,
        "customer_type": customer_type
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

print("customers.csv generated successfully")

# =====================================================
# PRODUCTS DATASET
# =====================================================

categories = {
    "Electronics": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Camera",
        "Headphones"
    ],
    "Clothing": [
        "T-Shirt",
        "Jeans",
        "Shoes",
        "Jacket",
        "Sweater"
    ],
    "Books": [
        "Novel",
        "Programming",
        "Science",
        "History",
        "Biography"
    ],
    "Home": [
        "Chair",
        "Table",
        "Lamp",
        "Cupboard",
        "Sofa"
    ]
}

products = []

NUM_PRODUCTS = 500

for i in range(NUM_PRODUCTS):

    product_id = f"P{i+1:04d}"

    category = random.choice(list(categories.keys()))

    product_name = random.choice(categories[category])

    subcategory = fake.word().title()

    cost_price = random.randint(100,80000)

    # Introduce inconsistent product names
    r = random.random()

    if r < 0.02:
        product_name = product_name.upper()

    elif r < 0.04:
        product_name = product_name.lower()

    elif r < 0.06:
        product_name = " " + product_name + " "

    products.append({
        "product_id": product_id,
        "product_name": product_name,
        "category": category,
        "subcategory": subcategory,
        "cost_price": cost_price
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    "data/raw/products.csv",
    index=False
)

print("products.csv generated successfully")

# =====================================================
# ORDERS DATASET
# =====================================================

NUM_ORDERS = 700

orders = []

status_list = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "RETURNED",
    "CANCELLED"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

for i in range(NUM_ORDERS):

    order_id = f"O{i+1:04d}"

    customer_id = random.choice(customers_df["customer_id"])

    order_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    status = random.choice(status_list)

    region = random.choice(regions)

    # ------------------------
    # Intentional Errors
    # ------------------------

    # 5% Missing Customer IDs
    if random.random() < 0.05:
        customer_id = None

    # 2% Future Dates
    if random.random() < 0.02:
        order_date = fake.date_between(
            start_date="+30d",
            end_date="+365d"
        )

    orders.append({
        "order_id": order_id,
        "customer_id": customer_id,
        "order_date": order_date,
        "status": status,
        "region": region
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    "data/raw/orders.csv",
    index=False
)

print("orders.csv generated successfully")


# ===========================================
# ORDER ITEMS DATASET
# ===========================================

NUM_ORDER_ITEMS = 1500

order_items = []

order_ids = orders_df["order_id"].tolist()
product_ids = products_df["product_id"].tolist()

for i in range(NUM_ORDER_ITEMS):

    item_id = f"I{i+1:04d}"

    order_id = random.choice(order_ids)

    product_id = random.choice(product_ids)

    quantity = random.randint(1, 5)

    unit_price = random.randint(100, 80000)

    discount_percent = random.randint(0, 40)

    # 2% Invalid Order IDs
    if random.random() < 0.02:
        order_id = "O9999"

    # 2% Negative Quantity
    if random.random() < 0.02:
        quantity = -1

    # 2% Invalid Discount
    if random.random() < 0.02:
        discount_percent = 120

    order_items.append({
        "item_id": item_id,
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_percent": discount_percent
    })

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    "data/raw/order_items.csv",
    index=False
)

print("order_items.csv generated successfully")