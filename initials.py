# Write a program that gets a string containing a person's first, middle, and last names, and then display their first, middle, and last initials. For example, if a person's name is John William Smith, then the program should display J.W.S.


#Create a function that asks the user for their first name and return their input.
def First_Name():
  first= input("What is your first name: ")
  return first

#Create a function that asks the user for their middle name and return their input.
def Middle_Name():
  middle= input("What is your middle name: ")
  return middle

#Create a function that asks the user for their last name and return their input.
def Last_Name():
  last= input("What is your last name: ")
  return last

#Create a function for the initials. To get someone's initials, we need their first, middle, and last name that we can pass as arguments in this function. To get the first letter of a person's name, we can create a for loop that will iterate through a string (the user's name) and we know that the first letter is at index 0 so we can store the name at index 0 in variables. Then combine the initials together in a variable to get the person's whole initials. Return initials.
def Initials(first,middle,last):
  for i in first:
    first_initial= first[0]
  for i in middle:
    middle_initial= middle[0]
  for i in last:
    last_initial= last[0]
  initials= first_initial + "." + middle_initial + "." +last_initial + "."
  return initials

#Store the functions in variables and satisfy any function that has argument requirements. The print() is used as a spacer so it is more readable. Then print the final statement you would like. Remember when doing concatenation, you have to convert variables to strings. 
def Main():
  first= First_Name()
  middle= Middle_Name()
  last= Last_Name()
  initials= Initials(first,middle,last)
  print()
  print("Your name is: " + str(first) + " " + str(middle) + " " + str(last)+ ". \nSo your initials are: " + str(initials))

#Don't forget to call the function.
Main()
