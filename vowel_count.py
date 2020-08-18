#Write a program to ask the user to enter a word and the program should return how many vowels are in the word.

#Create a variable to store the user's word
#Create another variable that will be used to count the number of vowels in the word
#Use a for loop to iterate through each character in the word and write a conditional statement to add 1 to vowel for each vowel in the word.
user_word=input("Please enter your lowercase word: ")
vowel=0
for i in user_word:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
    vowel+=1
print("Your word",user_word,"has",vowel,"vowels.")