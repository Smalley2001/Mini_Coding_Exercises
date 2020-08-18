print("You meet a group of aliens, and their language is just like English except that they say every word backwards. Write a program to convert the user's word so the aliens will understand.")
print()

#We need to ask the user for their word and then we are going to loop through it using the reversed() function. We will need a variable that will store each letter that the for loop iterates through and then print the reversed word.
reverse_word=""
user_word=input("Insert an english word: ")
for i in reversed(user_word):
  reverse_word+=i
print("Your word is",user_word)
print("The reverse of",user_word,"is",reverse_word)

#This code also works for constructing palindromes. Now that we created a program to change a word into its backwards orientation, we can use condiitonal statements to determine if the original word and the backwards word are exactly the same. IMPORTANT: if the user were to type in Dad (which is a palindrome) the computer would run the else statement because a capital "D" and a lowercase "d" are not the same. So, I created two new variables, one to store the lowercase version of the user_word and another to store the lowercase version of the reverse word. Because those are the same format, we can then check if they are the same. If they are, then we know the word is a palindrome. 
user_word_lowercase=user_word.lower()
reverse_word_lowercase=reverse_word.lower()
if user_word_lowercase==reverse_word_lowercase:
  print("The word",user_word,"is a palindrome.")
else:
  print(user_word,"is not a palindrome.")

