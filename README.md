This project simulates a food delivery platform with customers, restaurants, drivers, and orders. It uses Python + SQLite + Pandas + Matplotlib + scikit-learn to demonstrate a full data pipeline:
- Database creation
- Data loading
- SQL analysis
- Visualizations
- AI/ML predictions

---

## Project Structure

- customers.csv         # Fake customer data
- restaurants.csv       # Fake restaurant data
- drivers.csv           # Fake driver data
- orders.csv            # Fake order data
- setup_db.py           # Creates SQLite database & tables
- load_data.py          # Loads CSV files into the database
- analysis.py           # Runs SQL queries & prints insights
- visualizations.py     # Generates charts from analysis
- ml.py                 # Trains & evaluates AI model
- README.md             # Project documentation

Note: All of the "fake" data was created using ChatGPT

---

## How to Run

Run the scripts in the following order:

1. Create the database: `python3 setup_db.py`
2. Load CSV data into the database: `python3 load_data.py`
3. Run queries & see analysis: `python3 analysis.py`
4. Generate visualizations: `python3 visualizations.py`
5. Train & evaluate AI model: `python3 ml.py`

> Make sure to follow this order. The AI model (`ml.py`) depends on the data being present, and the visualizations depend on the analysis output.

---

## Requirements

Install the required Python packages once: `pip install pandas matplotlib scikit-learn`

---

## AI Component

The AI model is a linear regression model predicting delivery times using features such as order amount, driver rating, and restaurant type. It evaluates performance using Mean Absolute Error (MAE) and R² score.

---

## Features

- SQL Database for customers, restaurants, drivers, and orders
- Analysis queries (top customers, average delivery times, cuisine popularity)
- Visualizations with Matplotlib
- AI/ML model predicting delivery times

---

## Quick Run (All Steps)

To run the entire pipeline from scratch, copy-paste this single line-by-line sequence:

`python3 setup_db.py`  
`python3 load_data.py`  
`python3 analysis.py`  
`python3 visualizations.py`  
`python3 ml.py`

> Follow this exact order to ensure all scripts run correctly.