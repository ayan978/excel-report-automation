import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Create folders if they don’t exist
os.makedirs("data", exist_ok=True)

# 25+ realistic customer names
customers = [
    "Alice Smith", "Bob Johnson", "Carla Lee", "David King", "Eve Moore", "Frank Adams",
    "Grace Chen", "Henry Ford", "Isla Patel", "Jack Dawson", "Karen Li", "Liam White",
    "Maya Khan", "Noah Evans", "Olivia Ray", "Paul Green", "Quincy Blake", "Rita Paul",
    "Sophia Hill", "Tom Allen", "Uma Singh", "Victor Webb", "Wendy Scott", "Xander Liu",
    "Yara Bose", "Zach Trent", "Benjamin Cruz", "Natalie Ortiz"
]

# 12 product types
products = [
    "Monitor", "Keyboard", "Mouse", "Laptop", "Printer", "Webcam",
    "Tablet", "Router", "Desk Lamp", "External HDD", "USB Hub", "Smartphone"
]

def create_sales_file(filename, start_date, num_rows=500):
    rows = []
    for _ in range(num_rows):
        date = start_date + timedelta(days=random.randint(0, 27))
        customer = random.choice(customers)
        product = random.choice(products)
        qty = random.randint(1, 5)
        unit_price = random.choice([49.99, 79.99, 99.99, 129.99, 149.99, 199.99])
        # 5% chance of missing amount to simulate bad input
        amount = qty * unit_price if random.random() > 0.05 else ""
        rows.append([date, customer, product, qty, unit_price, amount])
    df = pd.DataFrame(rows, columns=["Date", "Customer", "Product", "Quantity", "Unit Price", "Amount"])
    df.to_excel(f"data/{filename}", index=False)

# Generate 500 rows per file = 1,000 total
create_sales_file("raw_sales_january.xlsx", datetime(2024, 1, 1), num_rows=500)
create_sales_file("raw_sales_february.xlsx", datetime(2024, 2, 1), num_rows=500)

print("✅ Input files created in 'data/' with 1,000 total records.")