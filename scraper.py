import pandas as pd
import os

os.makedirs("data", exist_ok=True)

df = pd.read_csv("source_companies.csv")
df.to_csv("data/raw_data.csv", index=False)

print("Raw data saved")