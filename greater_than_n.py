# In a program, write a function that accepts two arguments: a list, and a number n. Assume that the list contains numbers. The function should display all the numbers in the list that are greater than n.



#For this program, we can use a list of random numbers so in order to do that, we can import random.
import random

#Create a function that will return a list of random numbers. Create an empty list that will be used to add the random numbers. For this lab, I decided to let the list only include 10 elements so I put a for loop to iterate through a range of 1 to 11 so 10 would be included. Also, I decided to put a range of random numbers from 1 to 100. Append the random numbers to the list.
def Random_List():
  list_creation=[]
  for i in range(1,11):
    random_numbers= random.randint(1,100)
    list_creation.append(random_numbers)
  return list_creation

#Create a function to store any random number. Make a variable to store the random number and return the variable.
def Random_Number():
  n= random.randint(1,100)
  return n

#Create a function that creates the logic to determine which numbers in the list are larger than the random number. We have to pass a list and a number as arguments in this function. Create an empty list and store it in a variable so we can store the numbers greater than the random number in the list. Make a conditional statement to include the numbers greater than the random number and append them to the list.
def Greater_Number(list_creation,n):
  greater_than_list=[]
  for i in list_creation:
    if i>n:
      greater_than_list.append(i)
    else:
      None
  return greater_than_list

#Store the functions in variables and satisfy the argument requirements for those functions that need them. Print the statements to the console. The empty print() are used as spacers so it looks more readable.
def Main():
  random_list=Random_List()
  random_number=Random_Number()
  greater_number= Greater_Number(random_list,random_number)
  print("The list of random numbers is: " + str(random_list))
  print()
  print("The random number is: " + str(random_number))
  print()
  print("The list of numbers that are greater than " + str(random_number) + " is: " + str(greater_number))

#Don't forget to call the function
Main()
  
