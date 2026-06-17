import pandas as pd

def load_sales_data():
    try:
        sales = pd.read_csv("data/sales_promotions.csv")
        return sales
    except Exception as e:
        print("Error loading data:", e)
        return None
