import pandas as pd

# Step 1: Read the CSV file
cpd = pd.read_csv('D:\\jn\\marketing_campaign.csv',delimiter='\t')  # Use double backslashes or raw string

#renaming the columns
cpd=cpd.rename(columns= {'Year_Birth':'Birth_year'})
print(cpd.columns.tolist()) #check if the field name is changed


# Step 2: Convert object columns to numeric
cpd['ID'] = pd.to_numeric(cpd['ID'], errors='coerce')
cpd['Birth_year'] = pd.to_numeric(cpd['Birth_year'], errors='coerce')
cpd['Income'] = pd.to_numeric(cpd['Income'], errors='coerce')
cpd['Kidhome'] = pd.to_numeric(cpd['Kidhome'], errors='coerce')
cpd['Teenhome'] = pd.to_numeric(cpd['Teenhome'], errors='coerce')
cpd['Recency'] = pd.to_numeric(cpd['Recency'], errors='coerce')
cpd['MntWines'] = pd.to_numeric(cpd['MntWines'], errors='coerce')

# Step 3: Convert date column
cpd['Dt_Customer'] = pd.to_datetime(cpd['Dt_Customer'], format='%d-%m-%Y', errors='coerce')

# Step 4: Convert to categorical variables
cpd['Education'] = cpd['Education'].astype('category')         #use parentheses
cpd['Marital_Status'] = cpd['Marital_Status'].astype('category')

# check only incomplete columns
missing_cols=cpd.columns[cpd.isnull().any()]
print("colos with missing vlaues",missing_cols.tolist())
cpd = cpd.dropna(subset=['Income'])
print(cpd['Income'].isnull().sum())  # Should print 
print(cpd.shape)  # (rows, columns) 
print("Rows after dropping:", len(cpd))
print(cpd.isnull().values.any())  # Returns True if any NaNs exist, False if none
print(cpd.isnull().sum() == 0)
print("Total missing values:", cpd.isnull().sum().sum())

# Select only numeric columns
numeric_cols = cpd.select_dtypes(include=['number']).columns
# Fill NaNs in numeric columns only
cpd[numeric_cols] = cpd[numeric_cols].fillna(0)
#exporting as an excel file
cpd.to_excel('D:\\jn\\cleaned2_marketing_campaign.xlsx', index=False)








