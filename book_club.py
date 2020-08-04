# Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:

#If a customer purchases 0 books, he or she earns 0 points.
#If a customer purchases 2 books, he or she earns 5 points.
#If a customer purchases 4 books, he or she earns 15 points.
#If a customer purchases 6 books, he or she earns 30 points.
#If a customer pruchases 8 or more books, he or she earns 60 points.

#Write a program that asks the user to enter the number of books that he or she has purchased this month and displays the number of points awarded.

#Ask the user how many books they have

book_number= int(input("How many books did you purchase for the month: "))

#Make conditional statements for book numbers.

if book_number<2:
  print("You earned 0 points.")
elif book_number<4:
  print("You earned 5 points.")
elif book_number<6:
  print("You earned 15 points.")
elif book_number<8:
  print("You earn 30 points.")
else:
  print("You earn 60 points.")