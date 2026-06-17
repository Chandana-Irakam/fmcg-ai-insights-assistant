import pandas as pd


def load_sales_data():
    try:
        return pd.read_csv("data/sales_promotions.csv")
    except Exception as e:
        print("Error:", e)
        return None
