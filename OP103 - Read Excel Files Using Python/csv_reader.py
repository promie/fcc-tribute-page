# Import the csv module
import csv

# Open the csv file
f = open("sample_sales.csv",'rt')
reader = csv.reader(f)

# Read each line from csv file
for row in reader:
	    account_number = row[0]
	    account_name   = row[1]
	    sku            = row[2]
	    category       = row[3]
	    print (account_number,account_name,sku,category)
f.close()
