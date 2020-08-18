# A prime number is a number that is only evenly divisible by itself and 1. Write a boolean function named is_prime which takes an integer as an argument and returns true if the argument is a prime number, or false otherwise. Use the function in a program that prompts the user to enter a number that displays a message indicating the number is prime.

#Make a function that takes a number as an argument.
def is_prime(number):
   #Create a variable to be used as a counter to determine how many even divisions you get from the calculations
  evenDivisions= 0
  #Make conditonal statement to ensure that if a number is less than one then it automatically can't be prime so return False
  if number<=1:
    return False
    #Make a for loop that will check all the numbers between  from 1 to the user number. make sure you add 1 to user number just so the inputted number will be including in the range function calculation.
  for i in range(1, number + 1):
    #Use modulus to determine if the remainder is 0, if so, then it is even calculation and add 1 to the counting variable.
    if number % i==0:
      evenDivisions+= 1
      #Now since we know that a prime number can only have 2 even calculations, can only divide by itself and 1, if there are more than 2 calculations, then it can't be prime and return false. Otherwise, return true.
      if evenDivisions>2:
        return False
  return True

#Make another function to display the answer if a number is prime or not. Ask the user for a number. Store the previous function into a variable so it can be used. Check if the variable with the store function is true or not. Make conditional statements to determine what to display.

def Main():
  user_number= int(input("What number would you like to input: "))
  checker= is_prime(user_number)
  if checker==True:
    print(str(user_number) + " is a prime number.")
  else:
    print(str(user_number) + " is not a prime number.")

#Don't forget to call function
Main()


# Second programming challenge. Using the functions already created. Write a program that displays all of the prime numbers from 1 to 100. The program should have a loop that calls the is_prime function. 

#Make a function that has an empty list. Create a for loop that checks all the numbers from to 100. If the number satisfies the conditions in the is_prime function, meaning if the number makes is_prime is true, then append that number to the empty list. This will create a list of all prime numbers from 1 to 100.
def Answer():
  list=[]
  for m in range(1,101):
    if is_prime(m):
      list.append(m)
  print(list)

#Don't forget to call the function.
Answer()