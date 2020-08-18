# Design a program that generates a seven-digit lottery number. The program should generate seven random numbers, each in the range of 0 to 9, and assign each number to a list element. Then write another loop to that displays the contents of the list.

#To get random numbers, you need to import random
import random

#To create a list of the lottery numbers, create an empty list and store it in a variable.
lottery_numbers=7
lottery_list=[]
#To determine how many numbers to append to the list, create a for loop to iterate through a range of (1,8) so you will get seven numbers. Because, we want random numbers from 0 to 9, use random from 0 to 9 and store it in a variable to use. Then append each random number to the list within the for loop and print the results.
for i in range(1,8):
  number= random.randint(0,9)
  lottery_list.append(number)
print("Today's " + str(lottery_numbers) + " lottery numbers are: " + str(lottery_list))
