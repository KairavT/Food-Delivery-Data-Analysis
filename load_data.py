import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("food_delivery.db")
cursor = conn.cursor()

# Load CSVs into pandas DataFrames
customers = pd.read_csv("customers.csv")
restaurants = pd.read_csv("restaurants.csv")
drivers = pd.read_csv("drivers.csv")
orders = pd.read_csv("orders.csv")

# Insert into SQL (replace tables if they already exist)
customers.to_sql("customers", conn, if_exists="replace", index=False)
restaurants.to_sql("restaurants", conn, if_exists="replace", index=False)
drivers.to_sql("drivers", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)

# Quick check: count rows in each table
for table in ["customers", "restaurants", "drivers", "orders"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table};")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} rows inserted.")

conn.commit()
conn.close()