# LeadIntel – B2B Company Discovery Pipeline

A lightweight ETL pipeline that ingests company lead data, cleans records, stores them in SQLite, and exposes a searchable Streamlit dashboard.

## Tech Stack
- Python
- Pandas
- SQLite
- Streamlit

## Features
- Automated ETL pipeline
- Data cleaning & transformation
- SQLite database storage
- Search and filter dashboard
- CSV export download

## Project Structure
app.py            # Streamlit dashboard
scraper.py        # Data ingestion
clean.py          # Data cleaning
load_db.py        # Load data into SQLite
run_pipeline.py   # Runs complete pipeline

## How to Run

```bash
pip install -r requirements.txt
python run_pipeline.py
streamlit run app.py
