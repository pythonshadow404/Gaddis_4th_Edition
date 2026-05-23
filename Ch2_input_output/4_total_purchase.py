#4. Total Purchase
#input prices for five (5) items
item_1 = float(input("Enter price of item 1: "))
item_2 = float(input("Enter price of item 2: "))
item_3 = float(input("Enter price of item 3: "))
item_4 = float(input("Enter price of item 4: "))
item_5 = float(input("Enter price of item 5: "))

#calculate the subtotal of those five items
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
#Add 7% taxes
#display the subtotal, tax amount, and grand total
print(subtotal, '.2f')