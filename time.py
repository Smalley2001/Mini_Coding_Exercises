# Write a program that asks the user to enter a number of seconds and works as follows:

#There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the program should display the number of minutes in that many seconds.

#There are 3600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3600, the program should display the number of hours in that many seconds.

#There are 86400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86400, the program should display the number of hours in that many seconds.

#Ask the user how many seconds
seconds= float(input("Please enter a number of seconds: "))

#Convert the seconds
minutes= seconds/60
hours= seconds/3600
days= seconds/86400

#Make conditional statements for second conversions
if seconds<60:
  print("That is a total of: " + format(seconds, ".2f") + " seconds.")
elif seconds==60 or seconds<3600:
  print("That is a total of: " + format(minutes, ".2f") + " minutes.")
elif seconds==3600 or seconds<86400:
  print("That is a total of: " + format(hours, ".2f") + " hours.")
elif seconds>86400 or seconds==86400:
  print("That is a total of: " + format(days, ".2f") + " days.")
else:
  print("Restart the program.")
