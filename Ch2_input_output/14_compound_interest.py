# 14_compound_interest
principle = int(input("Enter the principle amount: "))
interest = float(input("Enter the interest amount: "))
years = int(input("Enter the number of years: "))
compounded_series = int(input("Enter the compounded series: "))
investment_amount = float(principle*(1 + (interest/compounded_series))**(compounded_series*years))
print(format(investment_amount, '.2f'))
