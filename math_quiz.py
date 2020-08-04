# Write a program that gives simple math quizzes. The program should display two random numbers that are added such as 247 + 129. The program should allow the student to enter the answer. If the answer is correct, a message of congratulations should be displayed. If the answer is incorrect, a message showing the correct answer should be displayed.

#To get the random numbers we need for the quiz, we are going to import random which will gives us all the numbers we want to use
import random

#We can store these numbers in a variables. The numbers inside the parenthesis indicate which range of numbers we would like to use. For this example, I chose (1,250)
first_random_number= random.randint(1,250)
second_random_number= random.randint(1,250)

#We want to make a function that asks the user a math question. We must declare that the variables we are mentioning in the function are the global variables so we must state global inside the function. 
def Ask_user_question():
  global first_random_number
  global second_random_number
  answer=int(input("What is " + str(first_random_number) + " + " + str(second_random_number) + "?: "))
  return answer

#We want a function that checks if the user number is equal to the correct answer. To do this, we can store the correct answer in a variable just by adding the number and use conditional statements to compare the user number as an agrument to the right answer.
def Answer_Checker(user_answer):
  global first_random_number
  global second_random_number
  Correct_Answer= first_random_number + second_random_number
  if Correct_Answer==user_answer:
    print("\nCongratulations, that is correct!")
  else:
    print("\nSorry, the correct answer is: " + str(Correct_Answer))

#Use the previous functions created and store them in variables in order to use them. 

def Main():
  Answer= Ask_user_question()
  correct_answer= Answer_Checker(Answer)
  print(correct_answer)

#Don't forget to call the function. 
Main()