import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# --- Step 1: Load data from SQLite ---
conn = sqlite3.connect("food_delivery.db")

query = """
SELECT o.amount, o.delivery_time, r.cuisine_type, d.rating
FROM orders o
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
JOIN drivers d ON o.driver_id = d.driver_id;
"""
df = pd.read_sql(query, conn)
conn.close()

print("Sample of training data:")
print(df.head(), "\n")

# --- Step 2: Preprocess data ---
# Convert categorical feature (cuisine_type) into numeric (one-hot encoding)
df = pd.get_dummies(df, columns=["cuisine_type"], drop_first=True)

X = df.drop("delivery_time", axis=1)  # Features
y = df["delivery_time"]               # Target

# --- Step 3: Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 4: Train model ---
model = LinearRegression()
model.fit(X_train, y_train)

# --- Step 5: Evaluate model ---
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f} minutes")
print(f"R² Score: {r2:.2f}")

# --- Step 6: Example prediction ---
example = X_test.iloc[0:1]  # take one test order
predicted_time = model.predict(example)[0]
print("\nExample Prediction:")
print("Features:", example.to_dict("records")[0])
print(f"Predicted delivery time: {predicted_time:.2f} minutes")
print(f"Actual delivery time: {y_test.iloc[0]} minutes")