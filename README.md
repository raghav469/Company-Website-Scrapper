# Company Website Finder

This Python script reads an Excel file containing company names, searches the web for their official websites, and saves the results into a new Excel file.

## Features
- Reads company names from an Excel file (`12.xlsx`)
- Searches for official websites (using DuckDuckGo search)
- Skips irrelevant sites (social media, Bloomberg, etc.)
- Saves results into a new file: `companies_with_websites.xlsx`
- Adds a `Website` column and a `Status` column for clarity

## Requirements
- Python 3.8+
- Libraries listed in `requirements.txt`

Install dependencies with:
```bash
pip install -r requirements.txt
