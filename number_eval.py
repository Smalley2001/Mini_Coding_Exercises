#In this lab, create a loop to repeatedly ask the user to input a number and the program will determine if the number is even, positive, odd, and calculate the sums. If the number is less than 0, the program shouldn't do anything. And if the user number is 0, then the program should display the results.

sum_of_odds=0
sum_of_evens=0
odd_count=0
even_count=0
positive_count=0
user_number= 3
while user_number !=0:
    user_number=int(input("Input an integer (0 terminates): "))
    if user_number<0:
        None
    if user_number==0:
        break
    if user_number>0:
        positive_count+=1
    if user_number%2==0 and user_number>0:
        even_count+=1
        sum_of_evens+=user_number
    if user_number%2!=0 and user_number>0:
        odd_count+=1
        sum_of_odds+=user_number
    else:
        None
print()
print("sum of odds:",sum_of_odds)
print("sum of evens:",sum_of_evens)
print("odd count:",odd_count)
print("even count:",even_count)
print("total positive int count:",positive_count)