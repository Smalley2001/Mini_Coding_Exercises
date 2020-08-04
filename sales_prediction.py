# A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks the user to enter the projected amount of total sales, and then displays the profit that will be made from that amount.

total_sales= float(input("What is your projected amount of total sales:"))
profit= 0.23 * total_sales
profit2= round(profit,2)
print("Your profit is: $" + str(profit2))



#You could also use the format function as well:
#total_sales= float(input("What is your projected amount of total sales:"))
#profit= 0.23 * total_sales
#print(format(profit, ",.2f"))