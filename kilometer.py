# Write a program that asks the user to enter a distance in kilometers, and then converts that distance to miles.

#This way ask the user for kilometers and stores that value in the miles variable times the conversion factor 0.6214
user_kilometers= float(input("What is the number of kilometers: "))
miles= user_kilometers * 0.6214
print(str(user_kilometers) + " kilometers is approximately " + format(miles, ".2f") + " miles.")

#Now using a function
def Converter(kilometers):
  miles2= kilometers * 0.6214
  print(str(kilometers) + " kilometers is equivalent to " + format(miles2, ".2f") + " miles.")

Converter(90)