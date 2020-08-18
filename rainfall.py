# Design a program that lets the user enter the total rainfall for each of the 12 months into a list. The program should calculate and display the total rainfall for the year, the average rainfall, and the highest and lowest amounts of rainfall. 


#Make a function that will store a list of all the user inputs for the year. Create an empty list that will contain the user_inputs. 
def User_Rainfall():
  rainfall_list=[]
  #Create a list that contains all the months and store it in a variable.
  months= ["January","February","March","April","May","June","July","August","September","October","November","December"]
  #Create a for loop in a range of the whole months list so just use len of months so the for loop will iterate through each element in the list. Inside the loop, ask the user to input the rainfall and instad of printing the index of months, you have to do months[i] to get the values. Add each user input to the empty list.
  for i in range (len(months)):
    user_input=float(input("How many milliliters of rainfall did you receive in " + str(months[i])+ ":"))
    rainfall_list.append(user_input)
  return(rainfall_list)

#Calculate the total rainfall, in order to do that, we need the list of the rainfall values as an argument in the function. We need to let a variable add up all the values in the list so let's set a variable that starts at zero and add up the inputs. The function should return the total.
def Total_Rainfall(rainfall_list):
  total=0
  for i in rainfall_list:
    total+=i
  return total

#To get the average, we can create a function that has the total rainfall as an argument. The average for the year is just the total divided by the 12 months. Return the average
def Average_Rainfall(total):
  average=total/12
  return average


#To get the highest amount, we can create a function that takes the rainfall amounts as an argument and returns the highest amount. To get the highest, we can use max, which will interpret which is the highest number in a list.
def Highest_Amount(amount):
  highest_rainfall=max(amount)
  return highest_rainfall

#To get the lowest amount, we can create a function that takes the rainfall amounts as an argument and returns the lowest amount. To get the lowest, we can use min, which will interpret which is the lowest number in a list.
def Lowest_Amount(amount):
  lowest_rainfall=min(amount)
  return lowest_rainfall

#To connect everything together, store the previous functions in variables. We can use the variable that stores the list of rainfall and pass it as an argument for the other functions that need an argument requirement. Then, print your final statement.
def Main():
  user_rainfall=User_Rainfall()
  total=Total_Rainfall(user_rainfall)
  average= Average_Rainfall(total)
  highest= Highest_Amount(user_rainfall)
  lowest= Lowest_Amount(user_rainfall)
  print("Your rainfall for each month was: " + str(user_rainfall) + " So, your total rainfall was for the year was: " + format(total,",.2f") + " millilters. And your average rainfall was: " + format(average,",.2f") + " milliliters. Your lowest rainfall was: " + str(lowest) + " millilters. And your highest rainfall was: " + str(highest) + " milliliters.")

#Don't forget to call the function.
Main()
