#The area of a rectangle is the rectangle's length times the width. Write a program that asks for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the same. 

#Rectangle 1
width1= float(input(" What is the width of the first rectangle: "))
height1= float(input("What is the height of the first rectangle: "))
area1= width1 * height1
print("The area of Rectangle 1 is: " + str(area1))

#Rectangle 2
width2= float(input(" What is the width of the second rectangle: "))
height2= float(input(" What is the height of the second rectangle: "))
area2= width2 * height2
print("The area of Rectangle 2 is: " + str(area2))

if area1>area2:
  print("Rectangle one has the bigger area.")
elif area2>area1:
  print("Rectangle two has the bigger area.")
else:
  print("The rectangles have the same area.")