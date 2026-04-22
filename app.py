import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="LeadIntel", layout="wide")

st.title("LeadIntel – B2B Company Discovery")
st.caption("Searchable lead database built with Python, Pandas, SQLite and Streamlit")

conn = sqlite3.connect("business.db")
df = pd.read_sql("SELECT * FROM leads", conn)

c1, c2, c3 = st.columns(3)
c1.metric("Total Leads", len(df))
c2.metric("Cities", df["city"].nunique())
c3.metric("Categories", df["category"].nunique())

st.divider()

search = st.text_input("Search Company")

col1, col2 = st.columns(2)

with col1:
    city = st.selectbox(
        "Filter City",
        ["All"] + sorted(df["city"].unique().tolist())
    )

with col2:
    category = st.selectbox(
        "Filter Category",
        ["All"] + sorted(df["category"].unique().tolist())
    )

if search:
    df = df[df["company_name"].str.contains(search, case=False, na=False)]

if city != "All":
    df = df[df["city"] == city]

if category != "All":
    df = df[df["category"] == category]

st.dataframe(df.reset_index(drop=True), width="stretch")

st.download_button(
    "Download Leads CSV",
    df.to_csv(index=False).encode("utf-8"),
    "filtered_leads.csv",
    "text/csv"
)