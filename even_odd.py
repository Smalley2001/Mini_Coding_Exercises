# Write a program that generates 100 random numbers and keeps a count of how many of those random numbers are even and how many of them are odd.

#To get random numbers we can import random
import random

#Create a function to store a random number. For this I chose from 1, 10 and I am going to going to iterate through this 100 times in another function.
def Random_Number_Generator():
  random_number= random.randint(1,10)
  return random_number

#This function determines if a number if even or not just by using the modulus operation to determine if there is a remiander.
def Even(number):
  if number % 2==0:
    return True
  return False

#This is the main part of the answer. I created two differet variables to count for each time we get an even or an odd number. I checked this in a range from 1 to 101 just to ensure we included 100. We can use the previous function by storing it in a variable and then pass that variable as an argument in the Even function. We can make a conditional statement to deterine if the Even function returns true, if it does, then add 1 to the even counter and if not, add 1 to the odd counter. Print results
def Main():
  even_counter= 0
  odd_counter= 0
  for i in range(1,101):
    random_number=Random_Number_Generator()
    if Even(random_number):
      even_counter +=1
    else:
      odd_counter+=1
  print("Out of a hundred, there are " + str(even_counter) + " even numbers and there are " + str(odd_counter) + " odd numbers.")
  
#Don't forget to call ac
Main()