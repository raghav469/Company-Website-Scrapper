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

```
This scrapper will give you the urls in this format == Found website: //duckduckgo.com/l/?uddg=https%3A%2F%2Fwww.zund.com%2Fen%2Fcompany%2Fsales%2Dnetwork%2Fzam&rut=3bc746712bb1c8c2b12ce7c95239cfb72ac7273b5a81512fe62420bd099b272a   soo to convert this in 
https format i have uploaded one file duck duckgo url to google url 
This will help you to get simple http url like this == https://www.zund.com/en/company/sales-network/zam

THANK YOU!!!
