# One foot equals 12 inches. Write a function named feet_to_inches that accepts a number of feet as an argument and returns the number of inches in that many feet. Use the function in a program that prompts the user to enter a number of feet and then displays the number of inches in that many feet. 

# Create function to store user feet input. This is not the only way to solve this problem, it's just a way to practice functions.
def ask_user():
  user_input= float(input("What is the number of feet: "))
  return user_input

#Create another function to store the inches conversion. We need an argument so we know how many feet will be converted to inches.
def Inches_Conversion(feet):
  inches= feet *12
  return inches

#Final answer. Use previous functions and store them in variables in order to use them. Print the final statment.
def feet_to_inches():
  feet= ask_user()
  Inches= Inches_Conversion(feet)
  print(format(feet,",.2f") + " feet is equivalent to: " + format(Inches, ",.2f") + " inches.")

#Don't forget to call the function. 
feet_to_inches()


