from pathlib import Path
import pandas as pd

data_path = Path("data/bike_buyers.csv.xls")  # your original file

# load data
try:
    df = pd.read_excel(data_path)
except Exception:
    # fallback if the file is actually CSV with a weird name
    df = pd.read_csv(data_path, encoding="utf-8", engine="python")

print("Before cleaning:", df.shape)

# Identify columns
text_cols = df.select_dtypes(include="object").columns
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

# Drop any row that has a missing value in *any* text column
before_rows = len(df)
df = df.dropna(subset=text_cols)
dropped_rows = before_rows - len(df)
print(f"Dropped rows due to missing text values: {dropped_rows}")

# Fill numeric nulls with column median
for col in num_cols:
    if df[col].isna().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

print("After cleaning:", df.shape)
print("\nRemaining nulls per column:")
print(df.isna().sum().to_string())

# Save to Excel (.xlsx). Note: pandas writes .xlsx (not old .xls).
out_path = Path("data/bike_buyers_clean.xlsx")
df.to_excel(out_path, index=False, sheet_name="cleaned")
print(f"\nSaved cleaned Excel → {out_path}")
