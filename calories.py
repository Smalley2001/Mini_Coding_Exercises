# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

# Make a list, make a for loop, convert to calories burned, and print each result

minutes= [10,15,20,25,30]
for i in minutes:
  calories= 4.2 * i
  print("You burned: " + str(calories) + " calories in " + str(i) + " minutes.")

# Another way to do it is using the range function
calories_burned_per_minute= 4.2
for m in range(10,31,5):
  calories_burned= (m/1) * calories_burned_per_minute
  print("You will burn, " + str(calories_burned) + " in " + str(m) + " minutes.")
