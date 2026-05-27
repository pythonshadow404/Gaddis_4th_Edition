#how much Joe paid for the stock
buy_price = float(input("Enter the stock buy price:"))
sell_price = float(input("Enter the stock sell price:"))
#principle
shares = 2000
#commission
commission = 0.03
initial_principle_commission = (shares*commission) * buy_price
final_principle_commission = (shares*commission) * sell_price

final_investment = final_principle_commission - initial_principle_commission
print(final_investment)

