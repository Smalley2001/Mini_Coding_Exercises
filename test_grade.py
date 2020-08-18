# Write a program that asks the user to enter five scores. The program should display a letter and the average test score. Write the following functions in the program:

#calc_average --- this function should accept five test scores as arguments and return the average of the scores. 

#determine_grade --- this function should accept a test score as an argument and return a letter grade for the score (on a standard grading scale.)


# Make a function to take five scores and return the average of the scores.
def calc_average(score1,score2,score3,score4,score5):
  total_score= score1 + score2 + score3 + score4 + score5
  average_score= total_score/5
  return average_score

# Create a function that takes a test score as an argument and make conditional statements to determine what grade corresponds.
def determine_grade(test_score):
  if test_score>90 or test_score==90:
    print("You got an A!")
  elif test_score==80 or test_score>80:
    print("You got a B!")
  elif test_score==70 or test_score>70:
    print("You got a C!")
  elif test_score==60 or test_score>60:
    print("You got a D!")
  else:
    print("You got an F!")

#Create a function that allows the user to input five scores. Input the scores as arguments in the calc_average function to get the average score. Store calc_average in a variable so we can use it. Then use that variable and pass it as an argument in the determine_grade function to generate which grade you got. Print final result. 
def Main():
  score1=float(input("What was your first score: "))
  score2=float(input("What was your second score: "))
  score3=float(input("What was your third score: "))
  score4=float(input("What was your fourth score: "))
  score5=float(input("What was your fifth score: "))
  average= calc_average(score1,score2,score3,score4,score5)
  print("Your average score is: " + str(average) + "%")
  determine_grade(average)

#Don't forget to call the function
Main()

