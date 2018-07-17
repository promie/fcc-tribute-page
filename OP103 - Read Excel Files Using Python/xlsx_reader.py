# Import pandas
import pandas as pd

# Convert excel to pandas dataframe
file = 'sample_sales.xlsx'
xl = pd.ExcelFile(file)
df = xl.parse('Sheet1')

counter = 0

# Read each line from pandas dataframe
for index, row in df.iterrows():
	account_number = row[0]
	account_name   = row[1]
	sku            = row[2]
	category       = row[3]
	counter += 1
	#print(account_number,account_name,sku,category)

print(counter)