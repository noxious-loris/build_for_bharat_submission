# data_fetcher.py
import pandas as pd
import os

# Load local CSVs
def load_rainfall_data():
    path = os.path.join(os.getcwd(), "Sub_Division_IMD_2017.csv")
    df = pd.read_csv(path)
    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def load_crop_data():
    path = os.path.join(os.getcwd(), "RS_Session_267_AU_1600_A_to_D.1.csv")
    df = pd.read_csv(path)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df
