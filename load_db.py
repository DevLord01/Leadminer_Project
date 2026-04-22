import pandas as pd, sqlite3
df=pd.read_csv("data/clean_data.csv")
conn=sqlite3.connect("business.db")
df.to_sql("leads", conn, if_exists="replace", index=False)
conn.close()
print("Database loaded")
