#One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to enter the total square feet in a tract of land and calculates the number of acres in the tract. Hint: Divide the amount entered by 43,560 to get the number of acres. 

square_feet= int(input("How many square feet are in your track of land: "))
oneAcreofLand= 43,560
acre_conversion= (square_feet / oneAcreofLand) *1
print(" You have " + str(acre_conversion) + "acres of land.")