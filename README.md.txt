# QueryFlow - MVP Documentation

## Purpose
A Power Query-like interface that compiles transformations into SQL.

## Features
- **SQL Backend:** Uses DuckDB for high-performance in-memory processing.
- **Applied Steps:** Mimics Power Query sidebar to track and modify transformations.
- **SQL Generation:** Translates UI actions into valid SQL queries automatically.

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run app: `streamlit run app.py`
