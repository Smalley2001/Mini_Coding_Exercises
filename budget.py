# Write a program that asks a user to enter the amount that he or she has budgeted for the month. A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total. When the loop finishes, the program should display the amount that the user is over or under the budget. 

print("Please enter your budget. You will then be asked to enter your expenses. Once you are done, type y")
print()

#We are going to need a variable that will store the expenses that the user inputs so we will set that variable to 0 first and then add the expenses to the variable in a loop. We need to ask the user what is the budget and store it in a variable. And we can store the difference between the budget and the expenses which can tell us later how much over or how much under the user spent. abs just means the absolute value
more_expenses="y"
user_sum=0
budget=float(input("What is your budget for the month: $"))


#Let's create a while loop to repeatedly ask the user what their expense is. And add each of their expenses to the variable that is counting the expenses (user_sum). Then set a variable that will continue to ask the user do they have more expenses. 
while more_expenses == "y":
  expense=float(input("Add your expense: "))
  user_sum= user_sum + expense
  more_expenses=input("Do you have anymore expenses: If yes, type y, if no, type n: ")

#Print your final expenses and budget
expense_and_budget_difference= abs(user_sum-budget)
print()
print("Your budget is: $" + format(budget,",.2f"))
print("Your total expenses is: $" + format(user_sum,",.2f"))

#Make conditional statements to determine if the total expenses are greater than, less than, or equal to the budget. 
if user_sum>budget:
  print("You exceeded your budget by: $" + str(expense_and_budget_difference))
elif budget>user_sum:
  print("You are under your budget by: $" + str(expense_and_budget_difference))
else:
  print("You used your exact budget.")