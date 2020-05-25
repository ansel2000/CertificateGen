import pandas as pd

x = pd.ExcelFile('CertName.xlsx')
# Dataframe of participants
names = pd.read_excel(x, 'Sheet1')

# For Testing
# names.head()
# f = open('test.txt', 'w')
# f.write(str(names))

# Extracting the names and category to lists
category = []
name = []
for h in names['Name:']:
    name.append(str(h))
for i in names['Category:']:
    category.append(str(i))
print(name)
print(category)
