#6_sales_tax
item = float(input("Enter item price: "))
state_tax = item * 0.05
local_tax = item * .025
total_price = item + state_tax + local_tax
print("Item Price", format(item, '.2f'))
print("State Tax: 5%")
print("County Tax: 2.5%")
print(format(total_price, '.2f'))
