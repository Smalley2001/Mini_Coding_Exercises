# A customer in a store is purchasing five items. Write a program that asks for the price of each item, and then displays the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 7%.
item1= float(input("What is the cost of your first item: "))
print( "Your subtotal is: " + str(round(item1,2)))
item2= float(input("What is the cost of your second item: "))
cost= item1 + item2
print( "Your subtotal is: " + str(round(cost,2)))
item3= float(input("What is the cost of your third item: "))
cost1= cost + item3
print( "Your subtotal is: " + str(round(cost1,2)))
item4= float(input("What is the cost of your fourth item: "))
cost2= cost1 + item4
print( "Your subtotal is: " + str(round(cost2,2)))
item5= float(input("What is the cost of your fifth item: "))
cost3= cost2 + item5
print( "Your subtotal is: " + str(round(cost3,2)))
sales_tax= 0.07 * cost3
print(" Your total sales tax is: " + str(round(sales_tax,2)))
final_cost=cost3 + sales_tax
print("Your total cost is: " + "$" + str(round(final_cost,2)))