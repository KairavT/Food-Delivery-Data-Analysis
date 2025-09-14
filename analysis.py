import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("food_delivery.db")

# Example 1: Top 5 customers by total spending
query_top_customers = """
SELECT c.name AS customer_name, SUM(o.amount) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 5;
"""
top_customers = pd.read_sql(query_top_customers, conn)
print("Top 5 Customers by Spending:")
print(top_customers, "\n")

# Example 2: Average delivery time per restaurant
query_avg_delivery = """
SELECT r.name AS restaurant_name, AVG(o.delivery_time) AS avg_delivery_time
FROM orders o
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY r.restaurant_id;
"""
avg_delivery = pd.read_sql(query_avg_delivery, conn)
print("Average Delivery Time per Restaurant:")
print(avg_delivery, "\n")

# Example 3: Number of orders per cuisine type
query_orders_cuisine = """
SELECT r.cuisine_type, COUNT(*) AS order_count
FROM orders o
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY r.cuisine_type;
"""
orders_cuisine = pd.read_sql(query_orders_cuisine, conn)
print("Orders per Cuisine Type:")
print(orders_cuisine)

# Close the connection
conn.close()