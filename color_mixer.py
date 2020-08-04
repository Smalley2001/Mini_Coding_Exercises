# The colors: red, blue, and yellow are known as primary colors becuase they cannot be made by mixing other colors. When you mix two primary colors, you get a secondary color as shown here:\

# When you mix red and blue, you get purple. When you mix red and yellow, you get orange. When you mix blue and yellow, you get green. 

# Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters anything other than red, blue, or yellow, the program should display an error message. Otherwise, the program should display the secondary color that results.


color_selection1= input("What is your first color: ")
color_selection2= input("What is your second color: ")
if (color_selection1=="Yellow" and color_selection2=="Red") or (color_selection1=="yellow" and color_selection2=="red"):
  print("The Secondary color is: Orange")
elif (color_selection1=="Yellow" and color_selection2=="Blue") or (color_selection1=="yellow" and color_selection2=="blue"):
  print("The Secondary color is: Green")
elif (color_selection1=="Blue" and color_selection2=="Red") or (color_selection1=="blue" or color_selection2=="red"):
  print("The Secondary color is: Purple")
elif (color_selection1=="Blue" and color_selection2=="Yellow") or (color_selection1=="blue" or color_selection2=="yellow"):
  print("The Secondary color is: Green")
elif (color_selection1=="Red" and color_selection2=="Blue") or (color_selection1=="red" and color_selection2=="blue"):
  print("The Secondary color is: Purple")
elif (color_selection1=="Red" and color_selection2=="Yellow")or (color_selection1=="red" and color_selection2=="yellow"):
  print("The Secondary color is: Orange")
else:
  print("Sorry, you did not pick two primary colors. Restart the program.")
