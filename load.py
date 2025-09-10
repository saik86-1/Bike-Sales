from pathlib import Path
import pandas as pd

# update this if your filename differs
data_path = Path("data/bike_buyers.csv.xls")

# Try reading as Excel first; if that fails, fall back to CSV
try:
    df = pd.read_excel(data_path)
except Exception as e:
    print(f"[read_excel failed] {e}\nFalling back to CSV...")
    df = pd.read_csv(data_path, encoding="utf-8", engine="python")

print("Shape (rows, cols):", df.shape)
print("\nColumns:", list(df.columns))

print("\nSample rows (first 10):")
print(df.head(10).to_string(index=False))

print("\nNulls per column:")
print(df.isna().sum().sum())
