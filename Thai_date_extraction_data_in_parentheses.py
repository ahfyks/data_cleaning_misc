import pandas as pd
import os
import re

# File path
os.chdir('C:/Users/dujnapa_tan/Documents/Budget Report/August 23/')

# Read the CSV file
df = pd.read_csv('input.csv', encoding='utf-8')

# Function to extract Thai date in the format "dd mmmm yy"
def extract_thai_date(text):
    # Use a regular expression to match the Thai date format (dd ก.ย. yy)
    match = re.search(r'(\d{1,2}\s[ก-๙a-zA-Z\'.]{4,5}\s\d{2,4})', text)
    
    if match:
        return match.group()
    else:
        return ''

# Function to extract data within parentheses
def extract_data_in_parentheses(text):
    match = re.search(r'\(([^)]+)\)[^(]*$', text)
    return match.group(1) if match else ''

#Function to remove both date and data in parentheses
def remove_date_parentheses(text):
    text_clean = text.replace(extract_thai_date(text),'').replace(extract_data_in_parentheses(text),'').replace(())
    return text_clean if text_clean else ''


# Apply the functions to the 'stage' column and store results in 'date' and 'เลขที่หนังสือ' columns
df['stage_clean']=df['stage'].apply(remove_date_parentheses)
df['date'] = df['stage'].apply(extract_thai_date)
df['เลขที่หนังสือ'] = df['stage'].apply(extract_data_in_parentheses)

# Write the results to a new CSV file with UTF-8 encoding
df.to_csv('output.csv', encoding='utf-8-sig', index=False)

print("Extraction completed and saved to output.csv.")