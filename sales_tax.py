# Write a program that will ask the user to enter the amount of a purchase. The program should then compute the state and county sales tax. Assume the state sales tax is 5 percent and the county sales tax is 2.5%. The program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of the purchase plus the total sales tax.)

purchase= float(input("What is the cost of your purchase: "))
state_tax= 0.05 * purchase
county_tax= 0.025 * purchase
total_tax= state_tax + county_tax
total_cost= total_tax + purchase
print(" You made a purchase that costs:  " + str(round(purchase,2)))
print("Your state tax is: $" + str(round(state_tax,2)))
print("Your county tax is: $" + str(round(county_tax,2)))
print("Your total tax is: $" + str(round(total_tax,2)))
print("Your total cost is: $" + str(round(total_cost,2)))

