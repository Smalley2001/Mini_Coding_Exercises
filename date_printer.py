# Write a program that reads a string from the user containing the date in the form mm/dd/yyyy. It should print the date in the form March 12, 2014. 

#Create a function to store the user date as a string.
def User_Date():
  user_date= input("Please enter the date in the form mm/dd/yyyy: ")
  return user_date

# Create a function that returns the appropriate month to the user date. We know date is in the format of mm/dd/yyyy. So for month, the index[0] and index[1] represents the month so make conditional statements based off those indexes to establish what month it is. REMEMBER establish the values as strings so don't put 0 because that's an integer, put "0" so it will be a string. return the variable that is storing the month. 
def Conversion_Month(date):
  if date[0]=="0" and date[1]=="1":
    month="January"
  elif date[0]=="0" and date[1]=="2":
    month= "February"
  elif date[0]=="0" and date[1]=="3":
    month= "March"
  elif date[0]=="0" and date[1]=="4":
    month= "April"
  elif date[0]=="0" and date[1]=="5":
    month= "May"
  elif date[0]=="0" and date[1]=="6":
    month= "June"
  elif date[0]=="0" and date[1]=="7":
    month= "July"
  elif date[0]=="0" and date[1]=="8":
    month= "August"
  elif date[0]=="0" and date[1]=="9":
    month= "September"
  elif date[0]=="1" and date[1]=="0":
    month= "October"
  elif date[0]=="1" and date[1]=="1":
    month= "November"
  elif date[0]=="1" and date[1]=="2":
    month= "December"
  else:
    None
  return month

# Create a functon to store the date. We know in mm/dd/yyyy, the date is represented in index[3] + index[4]. So let's store those indexes in a variable and return the variable.
def Conversion_Date(date):
  date_conversion= date[3] + date[4]
  return date_conversion

# Create a functon to store the date. We know in mm/dd/yyyy, the date is represented in index[6] + index[7] + index[8] + index[9]. So let's store those indexes in a variable and return the variable.
def Conversion_Year(date):
  year_conversion= date[6] + date[7] + date[8] + date[9]
  return year_conversion

#Store previous functions in variables and satisfy any argument requirements. print() is used as an empty spacer to make the lines more readable. Then print the final desired statement. \n means new line.
def Main():
  user_date=User_Date()
  month= Conversion_Month(user_date)
  date=Conversion_Date(user_date)
  year=Conversion_Year(user_date)
  print()
  print("You entered: " + str(user_date)+ "\nWhich means the date is: " + str(month) + " " + str(date) + "," + str(year))

#Don't forget to call the function.
Main()