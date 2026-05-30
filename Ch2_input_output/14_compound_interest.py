# 14_compound_interest
principle = float(input("Enter the principle amount: "))
interest = float(input("Enter the interest amount: "))
years = float(input("Enter the number of years: "))
compounded_series = float(input("Enter the compounded series: "))
investment_amount = principle(1 + (interest/compounded_series))**(compounded_series*years)
print(investment_amount)
