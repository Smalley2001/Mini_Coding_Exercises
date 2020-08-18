# Write a program that asks the user for the number of males and the number of females registered in a class. The program should display the percentage of males and females in the class. 

# Store the number of males, females, and total in different variables. 
user_males= int(input("How many males are in the class: "))
user_females= int(input("How many females are in the class: "))
user_total=int(input("What is the total number of students in the class: "))
#Store the percentages in separate variables. Remember to calculate percentage, you have to take a number and divide it by the total. Print the results.
males_percentage=user_males/user_total * 1
females_percentage=user_females/user_total * 1
print()
print("You have: " + str(user_males) + " males in the class. \nYou have: " + str(user_females) + " females in the class. \nThe total number of students in the class is " + str(user_total) + " students. \nThe male percentage rate is: " + format(males_percentage,",.2f") + "% \nThe female percentage rate is: " + format(females_percentage,",.2f") + "%")