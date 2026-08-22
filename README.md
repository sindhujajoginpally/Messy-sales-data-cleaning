# Messy Sales Data Cleaning (pandas)

An end-to-end data cleaning and analysis pipeline in pandas, applied to a realistically messy sales dataset.

## What it does
- Cleans a sales dataset with common real-world data quality issues: missing values, duplicate records, inconsistent text formatting, and mixed date formats
- Answers real business questions from the cleaned data: total revenue, top-performing city, best-selling product by volume

## Why I built it
Real business data is never clean. This project demonstrates the full, defensible cleaning workflow analysts actually use — including documenting *why* specific cleaning decisions were made, since different choices (e.g. filling missing values with the mean vs. the mode) produce different final numbers.

## Dataset issues handled
- Missing values (`Customer Name`, `Quantity`) — filled using justified strategies (mode over mean, to avoid unrealistic fractional values)
- Duplicate order records — identified and removed
- Inconsistent text casing/whitespace (`"MOUSE"` vs `"mouse "`) — standardized
- Mixed date formats (`2026-01-06` vs `2026/01/06`) — parsed into a consistent datetime format

## How to run it
```bash
pip install pandas
python messydata.py
```

## Key skills demonstrated
- pandas: `.isnull()`, `.fillna()`, `.drop_duplicates()`, `.str` methods, `pd.to_datetime()`, `.groupby()`, `.sort_values()`
- Data quality judgment: explaining tradeoffs between cleaning approaches, not just applying them
- Translating cleaned data into business-relevant insights

## Sample insight
Hyderabad generated the highest revenue ($110,000), nearly double the next closest city — a clear, decision-ready finding for a business stakeholder.
