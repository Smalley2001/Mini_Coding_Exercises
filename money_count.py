# Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The program should prompt the user to enter the number of pennies, nickels, dimes, and quarters. If the total value equals one dollar, the program should congratulate the user for winning the game. Otherwise, the game should display a message indicating if the amount entered was more or less than one dollar.

#Ask for number of coins
pennies= int(input(" How many pennies do you have: "))
nickels= int(input(" How many nickels do you have: "))
dimes= int(input(" How many dimes do you have: "))
quarters= int(input(" How many quarters do you have: "))

#Get value of each coin and total value
penny_value= 0.01 * pennies
nickel_value= 0.05 * nickels
dime_value= 0.1 * dimes
quarter_value= 0.25 * quarters
total_value= penny_value + nickel_value + dime_value + quarter_value

#Conditional statements total value 
if total_value==1:
  print(" Congratulations, your total was equal to one dollar. You won the game.")
elif total_value>1 :
  print(" Your total is " + format(total_value, ".2f") + " which is over a dollar. Please restart the program.")
elif total_value<1:
  print(" Your total is " + format(total_value, ".2f") + " which is under a dollar. Please restart the program.")