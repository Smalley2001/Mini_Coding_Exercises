# Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for food, and then calculate the amount of 18% tip and 7% sales tax. Display each of these amounts and the total.

user_meal=float(input("How much was your meal: "))
tip= user_meal * 0.18
sales_tax= user_meal * 0.07
total= user_meal + tip + sales_tax
print("Your meal costs: $" + format(user_meal,",.2f") + "\nAn 18% percent tip would be: $" + format(tip,",.2f") + "\nA 7% sales tax would be: $" + format(sales_tax,",.2f") +"\n So your total bill is: $" + format(total,",.2f"))