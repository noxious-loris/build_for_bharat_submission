# normalize.py
import pandas as pd

def normalize_rainfall(df: pd.DataFrame, metadata=None):
    df = df.copy()
    # Find likely year/state columns
    possible_state_cols = [c for c in df.columns if 'state' in c.lower() or 'sub_division' in c.lower()]
    possible_year_cols = [c for c in df.columns if 'year' in c.lower()]

    if possible_state_cols:
        df.rename(columns={possible_state_cols[0]: 'state'}, inplace=True)
    if possible_year_cols:
        df.rename(columns={possible_year_cols[0]: 'year'}, inplace=True)

    # Compute total rainfall if monthly columns exist
    monthly_cols = [c for c in df.columns if any(m in c.lower() for m in
        ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])]
    if monthly_cols:
        df['rainfall_mm'] = df[monthly_cols].sum(axis=1)

    df = df[['state', 'year', 'rainfall_mm']].dropna()
    df['year'] = df['year'].astype(int)
    return df


def normalize_crop(df: pd.DataFrame, metadata=None):
    df = df.copy()
    possible_state_cols = [c for c in df.columns if 'state' in c.lower()]
    possible_year_cols = [c for c in df.columns if 'year' in c.lower()]
    possible_crop_cols = [c for c in df.columns if 'crop' in c.lower()]
    possible_prod_cols = [c for c in df.columns if 'production' in c.lower() or 'prod' in c.lower()]

    if possible_state_cols:
        df.rename(columns={possible_state_cols[0]: 'state'}, inplace=True)
    if possible_year_cols:
        df.rename(columns={possible_year_cols[0]: 'year'}, inplace=True)
    if possible_crop_cols:
        df.rename(columns={possible_crop_cols[0]: 'crop'}, inplace=True)
    if possible_prod_cols:
        df.rename(columns={possible_prod_cols[0]: 'production'}, inplace=True)

    df = df[['state', 'year', 'crop', 'production']].dropna()
    df['year'] = df['year'].astype(int)
    return df
