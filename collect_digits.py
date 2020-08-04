#Collect Digits

#Given a string of any length, extract the numbers (digits) and print them on one line without spaces.

#For example, given this string:

#some 1! likes 2 put 14 digits, in 3 strings

#The output will be

#12143


#Ask the user to input a string. Let a variable store an empty string and let it add all the string charcaters that are digits. use the isdigit() method which checks to see if a string is a digit, if it is, return it will return true. If the iterable variable is a digit, add it to the empty string and print the new string at the end (outside of the loop)
s = input("Input a string: ")
answer=""
for i in s:
  if i.isdigit():
    answer+=i
print(answer)