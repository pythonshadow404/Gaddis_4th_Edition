#Prompt user to input total sales amount
total_sales = input("Enter projected total sales amount: ")
#Calculate the profit of 23% of total sales
profit = float(total_sales) * 0.23
#Display the profit with two decimal places 
# --format(12345.2578, '.2f')
print("Projected Profit: $", format(profit, '.2f'), sep='')