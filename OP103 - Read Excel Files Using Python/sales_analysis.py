# Import pandas
import pandas as pd

# Convert excel to pandas dataframe
file = 'sample_sales.xlsx'
xl = pd.ExcelFile(file)
df = xl.parse('Sheet1')

# Initialize sets to empty values
shoes = set()
belts = set()
shirts = set()

# Read each line from pandas dataframe and add items to sets
for index, row in df.iterrows():
        customer = (row[0],row[1])
        category = row[3]
        if category == "Shoes":
                shoes.add(customer)
        if category == "Belt":
                belts.add(customer)
        if category == "Shirt":
                shirts.add(customer)

# Print some analysis
print ("%s customers have purchased shoes" % len(shoes))
print ("%s customers have purchased belts" % len(belts))
print ("%s customers have purchased shoes but not belts" % len(shoes - belts))
print ("%s customers have purchased shoes and belts" % len(shoes & belts))
print ("%s customers have purchases shoes and shirts" % len(shoes & shirts))
print ("%s customers have purchased shoes, belts and shirts" % len(shoes & belts & shirts))
print ("The following customers are our most valued. They have purchased shoes & belts & shirts:")
for customer in shoes & belts & shirts:
        print (customer)