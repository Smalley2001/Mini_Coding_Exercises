# Many financial experts advise that property owners should insure thier homes or buildings for at least 80 percent of the amount it would cost to replace the structure. Write a program that asks the user to enter the replacement cost of a building and then displays the minimum amount of insurance he or she should buy for the property. 


#This activity is just a way to get comforatble with functions.

#This function is storing the user_input cost for the replacement that can be used later.
def Replacement_Cost():
  user_cost= float(input("How much does it cost to replace the structure: $"))
  return user_cost

#This is a function that stores the minimum recommended amount which is calculated by multiplying 80% to the user_cost
def Minimum_Amount(user_cost):
  minimum_insurance= user_cost * 0.80
  return minimum_insurance

#This function takes variables as arguments and will print the following statement for the user. This function is created to be used in the final function.
def printInformation(user_cost, minimum_insurance):
  print("It is advised that you should insure your property for $"+ format(minimum_insurance, ".2f") + " because it will be 80% of the replacement cost, which calculates to $" + format(user_cost, ".2f"))

#This is the final function in which we have to store the previous functioned with stored data into another variable so we can actually use it. By doing this, we can pass the new variables as arguments into the printInformation() function.
def main():
  replacement_cost= Replacement_Cost()
  minimumInsurance= Minimum_Amount(replacement_cost)
  printInformation(replacement_cost, minimumInsurance)

#Lastly, just remember to always call the function so it will run.
main()