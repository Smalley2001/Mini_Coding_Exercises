# A leap year in a Gregorian calendar system is a year that is divisible by 400 or a year divisible by 4 but not divisible by 100. Write a function that takes a string as an argument. If the string represents a leap year, return True else return False. 

def leap_year(year):
    if year.isdigit()==True:
        year=int(year)
    if (year%400==0) or (year%4==0 and year%100!=0):
        return True
    else:
        return False

print(leap_year('2014'))