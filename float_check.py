#Write a function that takes one a string as a parameter and prints True if the string is a float and False if otherwise. For the purpose of this function, we define float to be a string of digits that has at most, one decimal point. 

def float_check(string):
    counter=0
    while True:
      if string.isdigit()==True:
        print("True")
        break
      elif string.isdigit()==False and "." not in string:
        print("False")
        break
      for i in string:
          if i==".":
            counter=counter + 1
      if counter>1:
        print("False")
        break
      else:
        print("True")
        break