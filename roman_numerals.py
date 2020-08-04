# Write a program that prompts the user to enter a number within a range of 1 through 10. The program should display the Roman Numeral version of that number. If the number is outside 1 through 10, the program should display an error message. 

user_selection= int(input("Please pick a number from 1 to 10: "))
if user_selection== 1:
  print("The Roman Numeral version is: I")
elif user_selection==2:
  print("The Roman Numeral version is: II")
elif user_selection==3:
  print("The Roman Numeral version is: III")
elif user_selection==4:
  print("The Roman Numeral version is: IV")
elif user_selection==5:
  print("The Roman Numeral version is: V")
elif user_selection==6:
  print("The Roman Numeral version is: VI")
elif user_selection==7:
  print("The Roman Numeral version is: VII")
elif user_selection==8:
  print("The Roman Numeral version is: VIII")
elif user_selection==9:
  print("The Roman Numeral version is: IX")
elif user_selection==10:
  print("The Roman Numeral version is: X")
else:
  print("Error, your selection was not in the range of 1-10. Restart the program.")