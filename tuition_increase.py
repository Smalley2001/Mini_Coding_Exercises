# At one college, the tuition for a full-time student is $8000 per semester. It has been announced that the tuition will increase 3% each year for the next 5 years. Write a program with a loop that displays the projected semester tuition amount for the next 5 years.



#Make a variable to store tuition
#Create range function from 1-6 so it will cover the years 1 through 5. Remember, range doesn't include the last number.
#\t just means tab, which just spaces the information out
#\n means new line
#sep means separator which puts the dollar sign right next to the number to make it look real.

tuition= 8000
print("Year\ttuition\n----\t--------")
for i in range(1,6):
  tuition= tuition + (tuition * 0.03)
  print(i, "\t$",format(tuition, ".2f"), sep="")