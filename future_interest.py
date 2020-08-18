# Suppose you have a certain amount of money in a savings account that earns compound monthly interest, and you want to calculate the amount that you will have after a sepcific number of months. The formula is:

# F= P * (1+i)**t
# F means the future value of the account after the specified time period. P means the present value of account. i means the monthly interest. t is the number of months. 

#Write a program that prompts the user to enter the account's present value, monthly interest rate, and the number of months that the money will be left in the account. The program should pass these values to a function that returns the future value of the account, after the specified number of months. The program should display the account's future value. 

def Present_Value():
  present_value= float(input(" How much do you have in your savings account: "))
  return present_value

def Monthly_Interest():
  monthly_interest= float(input(" How much is your monthly interest: "))
  return monthly_interest

def Number_of_Months():
  months= float(input("How many more months will the money be left in the account: "))
  return months

def Future_Value(present,interest,months):
  future_value= present * (1+interest)**months
  return future_value

def Main():
  present_value= Present_Value()
  monthly_interest= Monthly_Interest()
  months= Number_of_Months()
  future_value= Future_Value(present_value,monthly_interest,months)
  print("If your account had a present value of: $" + format(present_value,",.2f") + " with a monthly interest of: $" + format(monthly_interest,",.2f") + " and with " + format(months, ",.2f") + " months left. Your future value will be: $" + format(future_value,",.2f"))

Main()

  