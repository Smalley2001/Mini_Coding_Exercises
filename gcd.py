# Ask the user to enter two numbers. Create a for loop in a range of (1,101), you can change the range but this will run from 1 to 100. Check if the user numbers modulo by the iteratable variable equals 0, then you know its a factor. 

user_number1= int(input("What is your first number: "))
user_number2= int(input("What is your second number: "))
for i in range(1,101):
  if (user_number1%i==0) and (user_number2%i==0):
    print("A factor is: ",i)
print()
#To get the greatest common factor, print i outside of the for loop because it will print i as its final value after running through the loop, which will be the greatest common factor. 
print("The greatest common factor is: ",i)