# A cookie recipe calls for the following ingredients: 1.5 cups of sugar, 1 cup of butter, and 2.75 cups of flour. The recipe produces 48 cookies with this amount of the ingredients. Write a program that asks the user how many cookies he or she wants to make, and then displays the number of cups of each ingredient needed for the specified number of cookies. 

user_cookies= int(input("How many cookies would you like to make: "))
butter= user_cookies * 1
flour= 2.75 * user_cookies
sugar= 1.5 * user_cookies 
print(" You want to make: " + str(user_cookies) + " cookies. \nYou would need: " + str(butter) + " cups of butter. \nYou would need: " + str(flour) + " cups.\nYou would need: " + str(sugar) + " cups.")