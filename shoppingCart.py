

# Round 1:
# Use Python to make a console application. 
# Parse the shopping cart CSV file and output: 
# 1. total price per category 
# 2. total price overall including 5% sales tax

# category,item,quantity,individual_price
# shirts,Blue Shirt,3,25.75
# shirts,Red Shirt,1,32.09
# pants,Jeans,4,87.00
# pants,Slacks,2,92.99



import csv
from collections import defaultdict


d = defaultdict(float)

with open('shopping_cart.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        d[line['category']] += float(line['individual_price'])

for category, total_price in d.items():
    print('{}: {}'.format(category, total_price))




x = csv.reader(open('shopping_cart.csv','rb'))
x.next()

total2 = 0
for row in x:  
	total2 += float(row[3])

salesTax = 0.05 * total2

totalPrice = total2 + salesTax

print "Total price overall including 5 percent sales tax: %s" %totalPrice

