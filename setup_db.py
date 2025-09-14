import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("food_delivery.db")
cursor = conn.cursor()

# Enable foreign keys in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Drop old tables if re-running (for a clean reset)
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("DROP TABLE IF EXISTS customers;")
cursor.execute("DROP TABLE IF EXISTS restaurants;")
cursor.execute("DROP TABLE IF EXISTS drivers;")

# Create Customers table
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    email TEXT UNIQUE
);
""")

# Create Restaurants table
cursor.execute("""
CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cuisine_type TEXT NOT NULL,
    city TEXT NOT NULL
);
""")

# Create Drivers table
cursor.execute("""
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rating REAL CHECK(rating >= 0 AND rating <= 5)
);
""")

# Create Orders table
cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    restaurant_id INTEGER,
    driver_id INTEGER,
    amount REAL NOT NULL,
    delivery_time INTEGER, -- in minutes
    order_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY(driver_id) REFERENCES drivers(driver_id)
);
""")

print("Database and tables created successfully!")

# Commit changes & close
conn.commit()
conn.close()
