# A car's miles per gallon (MPG) can be calculated with the following formula:

# MPG = Miles driven/ Gallons of gas used 

#Write a program that asks the user for the number of miles driven and the gallons of gas used. It should calculate the MPG and display the result

def MPG():
  miles_driven= float(input("How many miles did you drive: "))
  gallons_used= float(input("How many gallons of gas did you use: "))
  mpg= (miles_driven/gallons_used)*1
  print("Your MPG is: " + str(mpg) + " miles/gallon")

MPG()