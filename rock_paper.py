# Write a program that let's the user play the game of rock, paper, scissors, against the computer. If the user or the player picks #1, then they have chosen rock. If they pick #2, then it is paper. If they pick #3, then it is scissors. Set up the logic to the game and display the results. 


# We need to import random so I can get random numbers for the computer to pick.
import random

# Create a function that stores the user's choice. Make conditional statements to determine what each user choice represents. 
def User_Pick():
  user_choice= int(input("You are about to play rock paper scissors with the computer. Each number from 1 to 3 represent your options: 1= Rock, 2= Paper, 3= Scissors. Pick a number from 1 to 3: "))
  if user_choice==1:
    user_choice="Rock"
  elif user_choice==2:
    user_choice="Paper"
  else:
    user_choice="Scissors"
  return user_choice

#Create a function that stores the computer's selection. To do this use the random import to let the computer pick from 1 to 3. Make conditional statements to determine what each pick represents. 
def Computer_Pick():
  computer_choice= random.randint(1,3)
  if computer_choice==1:
    computer_choice="Rock"
  elif computer_choice==2:
    computer_choice="Paper"
  else:
    computer_choice="Scissors"
  return computer_choice

# Create a function that creates the logic for each result after the user and computer picks a number. This function will have two arguments to analyze, the user's choice and the computer's choice. Make conditional statements to represent the logic. Print the results for each variation.
def Selection_Winner(user_choice, computer_choice):
  if user_choice==computer_choice:
    print("You got a tie! ")
  elif user_choice=="Paper" and computer_choice=="Rock":
    print("You win!")
  elif user_choice=="Rock" and computer_choice=="Paper":
    print("You lose!")
  elif user_choice=="Paper" and computer_choice=="Scissors":
    print("You lose!")
  elif user_choice=="Scissors" and computer_choice=="Paper":
    print("You win!")
  elif user_choice=="Rock" and computer_choice=="Scissors":
    print("You win!")
  else:
    print("You lose")

#Put everything together. Store the previous functions as variables and passs the user's pick and computer's pick as arguments in the Selection_Winner function. print th results
def Main():
  user_choice= User_Pick()
  computer_choice= Computer_Pick()
  selection_winner= Selection_Winner(user_choice,computer_choice)
  print("You chose: " + str(user_choice) + " and the computer chose: " + str(computer_choice) + str(selection_winner) + ".")

#Don't forget to call the function
Main()
