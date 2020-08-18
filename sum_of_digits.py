# Write a program that asks the user to enter a series of single-digit numbers with nothing separating them. The program should display the sum of all the single-digit numbers in the string. For example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1, 4.

#Create a function that stores the user's input. Remember this number will be in the format of a string.
def User_Number():
  user_number= input("Please put in a number: ")
  return user_number

#Create a function that will store the sum of the user number's single-digits. To do this, we need a number as an argument (but it will be in the string format). Create a variable that will be used to add all the single-digits. Then, create a for loop that iterates through the string and create a variable that will convert each element to an integer while in the loop. Then add the integer version of the string to the initial variable created to store the sum. Return the sum
def Calculation(number):
  sum_of_numbers=0
  for i in number:
    integer_of_number= int(i)
    sum_of_numbers= sum_of_numbers + integer_of_number
  return sum_of_numbers

#Store the previous functions in variable and satisfy any argument requirement. The print() is used as a spacer so it will be read better. Print your final desired statement. \n just means new line.
def Main():
  user_number=User_Number()
  calculation=Calculation(user_number)
  print()
  print("Your number was: " + str(user_number) + "\nThe sum of the single-digits is: " + str(calculation))

#Don't forget to call the function. 
Main()


# Another way to solve this is using using Index

#This remains exactly the same. I just change the function and variable name to avoid confusion.
def User_Input():
  user_input= input("Please put in a number: ")
  return user_input

#Create a function to calculate the sum of single-digits. We still create a variable that wil store the single-digits. Now use a for loop in range of the length of a string (which will be a number) and create a variable that will store the value of the element beased off of it's index (line 38). Create another variable that converts the value into an integer. Both of these variables should be in the for loop. The add the integer version of the digits to the variable that is counting the sum. Return the sum of the digits. 
def Math_Calculation(number):
  sum_of_numbers=0
  for i in range(len(number)):
    digit_string= number[i]
    digit_number= int(digit_string)
    sum_of_numbers= sum_of_numbers + digit_number
  return sum_of_numbers

#This is exactly the same. I just used different variables and a different function name to avoid confusion.
def Solution():
  user_input=User_Input()
  calculation=Math_Calculation(user_input)
  print()
  print("The number is: " + str(user_input) + "\nThe sum of the single-digits is: " + str(calculation))

#Don't forget to call the function
Solution()