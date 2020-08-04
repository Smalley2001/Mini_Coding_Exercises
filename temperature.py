# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula goes as follows:

# F= (9/5)C + 32

#The program should ask the user to enter a temperature in Celsius, and then display the temperature converted to Fahrenheit. 

def temperature():
  celsius= float(input(" What is the temperature in celsius: "))
  fahrenheit= (9/5)*celsius + 32
  print("The temperature in Fahrenheit is: " + str(fahrenheit) + " degrees.")
temperature()