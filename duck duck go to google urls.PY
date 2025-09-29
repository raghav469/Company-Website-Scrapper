import pandas as pd
import urllib.parse
import re

# Load the Excel file
file_path = "companies_with_websites.xlsx"  
df = pd.read_excel(file_path)

# Function to clean URLs
def clean_url(url):
    if isinstance(url, str):
        # Decode URL encoding
        decoded_url = urllib.parse.unquote(url)
        
        # Extract the main URL before any parameters
        match = re.search(r"https?://[^\s&]+", decoded_url)
        
        return match.group(0) if match else decoded_url
    return ""  # Return empty string or original value if not a string

# Apply the cleaning function to the "Website" column
df["Website"] = df["Website"].apply(clean_url)

# Save the cleaned URLs as a plain text file
plain_text_file = "simple_urls.csv"
with open(plain_text_file, "w", encoding="utf-8") as file:
    file.write("\n".join(df["Website"].tolist()))

print(f"Clean URLs saved to {plain_text_file}")
