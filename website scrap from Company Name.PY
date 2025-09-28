import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import quote
import re


def search_company_website(company_name):
    """Search for company website using DuckDuckGo"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # Encode the company name for the search URL
    search_query = quote(f"{company_name} official website")
    url = f"https://duckduckgo.com/html/?q={search_query}"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for results
        results = soup.find_all('div', class_='result')
        
        for result in results:
            
            link = result.find('a', class_='result__url')
            if link and link.get('href'):
                url = link.get('href')
                # Skip social media and similar sites
                skip_sites = ['facebook.com', 'linkedin.com', 'twitter.com', 
                            'instagram.com', 'youtube.com', 'bloomberg.com']
                if not any(site in url.lower() for site in skip_sites):
                    return url
    except Exception as e:
        print(f"Error searching for {company_name}: {str(e)}")
    return None

def process_excel():
    try:
        # Read the Excel file
        print("Reading 12.xlsx...")
        df = pd.read_excel("12.xlsx")
        
        
        # Print column names
        print("\nAvailable columns:", df.columns.tolist())
        
        # Find the company name column
        company_columns = [col for col in df.columns if any(word in col.lower() 
                         for word in ['company', 'name', 'firma', 'empresa'])]
        
        if not company_columns:
            print("\nCouldn't find company name column. Please enter the column name:")
            print("Available columns:", df.columns.tolist())
            return
            
        company_column = company_columns[0]
        print(f"\nUsing column: {company_column}")
        
        # Add website column
        df['Website'] = ''
        df['Status'] = ''
        
        # Process each company
        total = len(df)
        for index, row in df.iterrows():
            company_name = str(row[company_column]).strip()
            print(f"\nProcessing {index + 1}/{total}: {company_name}")
            
            if pd.isna(company_name) or company_name == '':
                print("Empty company name - skipping")
                continue
                
            website = search_company_website(company_name)
            
            if website:
                print(f"Found website: {website}")
                df.at[index, 'Website'] = website
                df.at[index, 'Status'] = 'Success'
            else:
                print("No website found")
                df.at[index, 'Status'] = 'Not found'
            
            # Wait between requests
            time.sleep(2)
        
        # Save results
        output_file = 'companies_with_websites.xlsx'
        df.to_excel(output_file, index=False)
        print(f"\nResults saved to {output_file}")


        # Print summary
        successful = len(df[df['Status'] == 'Success'])
        print(f"\nSummary:")
        print(f"Total companies processed: {total}")
        print(f"Successful website finds: {successful}")
        print(f"Success rate: {(successful/total)*100:.2f}%")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("Starting website search process...")
    process_excel() 
    