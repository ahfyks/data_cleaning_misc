import json
import pandas as pd
import os as os

# File path
os.chdir('YOUR FILE PATH')

# Load the JSON data from your file
with open('documents-2023-08-22T115703.json', 'r',encoding='utf-8') as json_file:
    data = json.load(json_file)

# Create a list to store the filtered data
filtered_data = []
# Create a dictionary to keep track of budget sums for each code_th
code_th_sums = {}

# Iterate through the data and filter based on the conditions
for item in data:
    _id_oid = item.get('_id', {}).get('$oid')
    fiscal_year = item.get('fiscal_year')
    org_l1 = item.get('org_l1')
    org_l2 = item.get('org_l2')
    org_l3 = item.get('org_l3')
    code_th = item.get('code_th')
    budget_sum = item.get('budget_sum')
    budget_sum_plan = item.get('budget_sum_plan')
    
    # Check if budget_sum is not equal to budget_sum_plan
    if budget_sum != budget_sum_plan:
        filtered_data.append({
            '_id.$oid': _id_oid,
            'fiscal_year': fiscal_year,
            'org_l1': org_l1,
            'org_l2': org_l2,
            'org_l3': org_l3,
            'code_th': code_th,
            'budget_sum': budget_sum,
            'budget_sum_plan': budget_sum_plan
        })
    
      # Check if budget_sum and budget_sum_plan are normally equal for one code_th
    if code_th in code_th_sums:
        if code_th_sums[code_th] != budget_sum:
            # Budget sums for the same code_th are not equal, so remove the flag
            del code_th_sums[code_th]
    else:
        # Set the initial budget sum for this code_th
        code_th_sums[code_th] = budget_sum

# Create a DataFrame from the filtered data        
filtered_data_df = pd.DataFrame(filtered_data)

        
# Export the filtered data to an Excel file with UTF-8-SIG encoding
filtered_data_df.to_excel('filtered_data.xlsx', index=False)
print("Filtering process completed and saved to filtered_data.xlsx.")
