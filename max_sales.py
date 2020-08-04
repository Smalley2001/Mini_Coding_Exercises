# Write a function named max that accepts two integer values as arguments and returns the value that is the greater of the two. Use the function in a program that prompts the user to enter two values. The program should display the value that is the greater of the two. 


#Make a function that takes two numbers as arguments. Use conditional statements to determine which number is larger and return that number.
def Max(number1,number2):
  if number1> number2:
    return number1
  elif number2> number1:
    return number2
  else:
    None


#Now create another functon where you allow the user to input the two numbers. Store the previous function with the user numbers as its arguments in a variable so I can use it. Make conditional statements to determine which number is greater. 

def Main():
  first_number= int(input("What is your first number: "))
  second_number= int(input("What is your second number: "))
  checker= Max(first_number,second_number)
  if checker==first_number:
    print(str(first_number) + " is greater than " + str(second_number))
  elif checker==second_number:
    print(str(second_number) + " is greater than " + str(first_number))
  else:
    print("Both numbers are equal.")

#Don't forget to call the function. 
Main()

