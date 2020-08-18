# Design a program that asks the user to enter a series of 20 numbers. The program should store the numbers in a list and then display: the lowest number in a list, the highest number in a list, the total of the numbers in the list, the average of the numbers in the list. 


#Create a function to store the user's numbers. Make an empty list and store it in a variable so we can append the user's numbers into the list. Becuase the directions said 20 numbers make a for loop in range of (1,21) to include 20. return the list with the user's numbers. 
def User_Number():
  list_of_numbers=[]
  for i in range(1,21):
    user_number=float(input("Please enter number " + str(i)+ " :"))
    list_of_numbers.append(user_number)
  return list_of_numbers

#Make a function that will store the lowest number. We need a list as an argument in order to determine which element is the lowest. Use min to get minimum value and store in a variable. Return the variable.
def Lowest_Number(number_list):
  lowest_number= min(number_list)
  return lowest_number

#Make a function that will store the highest number. We need a list as an argument in order to determine which element is the highest. Use max to get minimum value and store in a variable. Return the variable.

def Highest_Number(number_list):
  highest_number= max(number_list)
  return highest_number

# Create a function that will store the total value of a list. To do this we need a list as an argument and a variable to add the elements up and store the sum. We need a for loop to iterate througb each element of the list and add it to the variable. Return the total
def Total(number_list):
  total=0
  for i in number_list:
    total+=i
  return total

# An Average is the total or sum of numbers divided by how many numbers are being added. Create a function that will return the average. We need to know the total of the numbers and how many numbers are being added and pass them as arguments. Because one of the arguments is a list we can divide by the len of a list in order to know how many elements are being added.
def Average(total,user_number):
  average= total/len(user_number)
  return average

# Take all the functions and store them in variables accordingly. Then create your statements you would like to print. The empty print() are used as spacers that simply divide the sentences so they are more easily readable. 
def Main():
  user_number= User_Number()
  lowest_number=Lowest_Number(user_number)
  highest_number= Highest_Number(user_number)
  total= Total(user_number)
  average= Average(total, user_number)
  print()
  print("Your list of 20 numbers are: " + str(user_number))
  print()
  print("The lowest number in the list is: " + str(lowest_number))
  print()
  print("The highest number in the list is: " + str(highest_number))
  print()
  print("The total value is: " + str(total))
  print()
  print("The average value is: " + str(average))

#Don't forget to call the function. 
Main()