# Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase: 

# The number of shares that Joe purchased was 2,000.
# When Joe purchased the stock, he paid $40.00 a share.
# Joe paid his stock broker a commission that amounted to 3% of the amount he paid for the stock.

#Two weeks later, Joe sold the stock. Here are the details of the sale:

#The number of shares Joe sold was 2,000.
#He sold the stock for $42.75 a share.
#He paid his stock broker another commission that amounted to 3% of the amount he receieved from the stock.

#Write a program that displays the following information:
#The amount of money Joe paid for the stock
#The amount of commission he paid the stock broker when he purchased the stock
#The amount Joe sold the stock for
#The amount of commission Joe paid the stock broker when he sold the stock
#Display the amount of money that Joe had left when he sold the stock and paid his broker (both times). If this amount is positive then Joe made a profit, if it is negative, then Joe lost money.

shares_purchased= 2000
cost_per_share= 40.00
total_cost_of_purchase= shares_purchased * cost_per_share
broker_commission_for_purchase= 0.03 * total_cost_of_purchase
shares_sold= 2000
selling_price_per_share= 42.75
total_amount_received= shares_sold * selling_price_per_share
broker_commission_for_sell= 0.03 * total_amount_received
total_broker_commission= broker_commission_for_purchase + broker_commission_for_sell
remaining_balance= total_amount_received- total_cost_of_purchase- total_broker_commission
print("Your purchase costs: $" + str(total_cost_of_purchase))
print("You paid the broker: $" + str(broker_commission_for_purchase) + " for your purchase.")
print("You sold the stock for: $" + str(total_amount_received))
print("You paid the broker: $" + str(broker_commission_for_sell) + " for sell.")
print(" You paid the broker a total amount of: $" + str(total_broker_commission))
print("The total amount of money you have left is: $" + str(remaining_balance))
if remaining_balance>0:
  print("You made a profit of: $" + str(remaining_balance))
else:
  print("You lost: $" + str(remaining_balance))