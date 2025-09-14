import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite
conn = sqlite3.connect("food_delivery.db")

# --- Query 1: Top 5 Customers by Spending ---
query_top_customers = """
SELECT c.name AS customer_name, SUM(o.amount) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 5;
"""
top_customers = pd.read_sql(query_top_customers, conn)

plt.figure(figsize=(6,4))
plt.bar(top_customers["customer_name"], top_customers["total_spent"], color="skyblue")
plt.title("Top 5 Customers by Spending")
plt.xlabel("Customer")
plt.ylabel("Total Spent ($)")
plt.tight_layout()
plt.show()
plt.close()


# --- Query 2: Average Delivery Time per Restaurant ---
query_avg_delivery = """
SELECT r.name AS restaurant_name, AVG(o.delivery_time) AS avg_delivery_time
FROM orders o
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY r.restaurant_id;
"""
avg_delivery = pd.read_sql(query_avg_delivery, conn)

plt.figure(figsize=(6,4))
plt.bar(avg_delivery["restaurant_name"], avg_delivery["avg_delivery_time"], color="salmon")
plt.title("Average Delivery Time per Restaurant")
plt.xlabel("Restaurant")
plt.ylabel("Avg Delivery Time (min)")
plt.tight_layout()
plt.show()
plt.close()


# --- Query 3: Orders per Cuisine Type ---
query_orders_cuisine = """
SELECT r.cuisine_type, COUNT(*) AS order_count
FROM orders o
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY r.cuisine_type;
"""
orders_cuisine = pd.read_sql(query_orders_cuisine, conn)

plt.figure(figsize=(6,4))
plt.bar(orders_cuisine["cuisine_type"], orders_cuisine["order_count"], color="lightgreen")
plt.title("Orders per Cuisine Type")
plt.xlabel("Cuisine Type")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()
plt.close()

# Close connection
conn.close()