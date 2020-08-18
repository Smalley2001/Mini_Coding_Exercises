#This activity converts a decimal number to a binary number but only up to 
# 2 **10. Write a program that asks the user for a decimal number and return
#the binary number. 

user_decimal_number= int(input("Enter a number: "))
binary=""

#In this while loop, it will take the user number and subtract the given value
#to see if the value will be over or equal to 0, if it is, add 1 to the binary
#variable, if the difference between the user number and the value will be less
#than 0, add a 0 to binary. Make sure to break the while loop after computing
#2**0 and print the binary conversion. 
while True:
    if user_decimal_number-(2**10)>=0:
        binary+="1"
        user_decimal_number-=(2**10)
    else:
        binary+="0"
    if user_decimal_number-(2**9)>=0:
        binary+="1"
        user_decimal_number-=(2**9)
    else:
        binary+="0"
    if user_decimal_number-(2**8)>=0:
        binary+="1"
        user_decimal_number-=(2**8)
    else:
        binary+="0"
    if user_decimal_number-(2**7)>=0:
        binary+="1"
        user_decimal_number-=(2**7)
    else:
        binary+="0"
    if user_decimal_number-(2**6)>=0:
        binary+="1"
        user_decimal_number-=(2**6)
    else:
        binary+="0"
    if user_decimal_number-(2**5)>=0:
        binary+="1"
        user_decimal_number-=(2**5)
    else:
        binary+="0"
    if user_decimal_number-(2**4)>=0:
        binary+="1"
        user_decimal_number-=(2**4)
    else:
        binary+="0"
    if user_decimal_number-(2**3)>=0:
        binary+="1"
        user_decimal_number-=(2**3)
    else:
        binary+="0"
    if user_decimal_number-(2**2)>=0:
        binary+="1"
        user_decimal_number-=(2**2)
    else:
        binary+="0"
    if user_decimal_number-(2**1)>=0:
        binary+="1"
        user_decimal_number-=(2**1)
    else:
        binary+="0"
    if user_decimal_number-(2**0)>=0:
        binary+="1"
        user_decimal_number-=(2**0)
    else:
        binary+="0"
    print("The binary conversion is: ", binary)
    break
