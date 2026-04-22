import pandas as pd

df = pd.read_csv("data/raw_data.csv")

df.drop_duplicates(inplace=True)

df["company_name"] = df["company_name"].fillna("Unknown").str.strip()
df["city"] = df["city"].fillna("Unknown").str.title()
df["category"] = df["category"].fillna("General").str.strip()
df["rating"] = pd.to_numeric(df["rating"], errors="coerce").fillna(0)
df["website"] = df["website"].fillna("N/A")
df["phone"] = df["phone"].fillna("N/A")
df["employees"] = pd.to_numeric(df["employees"], errors="coerce").fillna(0)

df.to_csv("data/clean_data.csv", index=False)

print("Clean data saved")