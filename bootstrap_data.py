# bootstrap_data.py
import pandas as pd
import qa_engine

# Local CSVs
RAIN_FILE = "RS_Session_267_AU_1600_A_to_D.1.csv"
CROP_FILE = "Sub_Division_IMD_2017.csv"

print("Loading local CSVs...")
rainfall_df = pd.read_csv(RAIN_FILE)
crop_df = pd.read_csv(CROP_FILE)

print("Cleaning and preparing data...")

# --- Normalize rainfall ---
# Adjust columns if your CSV differs
rainfall_df = rainfall_df.rename(columns=lambda c: c.strip().lower())
if "year" not in rainfall_df.columns:
    # infer year column if needed
    possible_year_cols = [c for c in rainfall_df.columns if "year" in c]
    if possible_year_cols:
        rainfall_df["year"] = rainfall_df[possible_year_cols[0]]

# --- Normalize crop data ---
crop_df = crop_df.rename(columns=lambda c: c.strip().lower())
if "year" not in crop_df.columns:
    possible_year_cols = [c for c in crop_df.columns if "year" in c]
    if possible_year_cols:
        crop_df["year"] = crop_df[possible_year_cols[0]]

# Convert numeric columns
for col in ["rainfall", "production"]:
    if col in rainfall_df.columns:
        rainfall_df[col] = pd.to_numeric(rainfall_df[col], errors="coerce")
    if col in crop_df.columns:
        crop_df[col] = pd.to_numeric(crop_df[col], errors="coerce")

# Store into qa_engine
qa_engine.set_dataframes(rainfall_df, crop_df)

print("✅ Data loaded and ready.")
