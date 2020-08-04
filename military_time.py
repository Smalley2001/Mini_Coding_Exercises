print("This program will convert a standard time to military time. For example, if you put 10:00 pm, the program will return 2200")
print()

#Create a variable that will ask the user to input a time. Remember this will be a string. Because it's a string we can use conditional statements to check if the index of a string equals a certain value. Keep in mind that some strings such as 10:00 pm has one more character than 1:00 pm so the indexes are different. You also have to make sure to check if the user time is in am or pm. 

user_time=input("Please insert the time: ")
if user_time[0]=="1" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 01"+user_time[2]+user_time[3])
elif user_time[0]=="2" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 02"+user_time[2]+user_time[3])
elif user_time[0]=="3" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 03"+user_time[2]+user_time[3])
elif user_time[0]=="4" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 04"+user_time[2]+user_time[3])
elif user_time[0]=="5" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 05"+user_time[2]+user_time[3])
elif user_time[0]=="6" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 06"+user_time[2]+user_time[3])
elif user_time[0]=="7" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 07"+user_time[2]+user_time[3])
elif user_time[0]=="8" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 08"+user_time[2]+user_time[3])
elif user_time[0]=="9" and user_time[1]==":" and user_time[5]=="a":
  print(user_time+" is equal to 09"+user_time[2]+user_time[3])
elif user_time[0]=="1" and user_time[1]=="0" and user_time[6]=="a":
  print(user_time+" is equal to 10"+user_time[3]+user_time[4])
elif user_time[0]=="1" and user_time[1]=="1" and user_time[6]=="a":
  print(user_time+" is equal to 11"+user_time[3]+user_time[4])
elif user_time[0]=="1" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 13"+user_time[2]+user_time[3])
elif user_time[0]=="2" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 14"+user_time[2]+user_time[3])
elif user_time[0]=="3" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 15"+user_time[2]+user_time[3])
elif user_time[0]=="4" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 16"+user_time[2]+user_time[3])
elif user_time[0]=="5" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 17"+user_time[2]+user_time[3])
elif user_time[0]=="6" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 18"+user_time[2]+user_time[3])
elif user_time[0]=="7" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 19"+user_time[2]+user_time[3])
elif user_time[0]=="8" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 20"+user_time[2]+user_time[3])
elif user_time[0]=="9" and user_time[1]==":" and user_time[5]=="p":
  print(user_time+" is equal to 21"+user_time[2]+user_time[3])
elif user_time[0]=="1" and user_time[1]=="0" and user_time[6]=="p":
  print(user_time+" is equal to 22"+user_time[3]+user_time[4])
elif user_time[0]=="1" and user_time[1]=="1" and user_time[6]=="p":
  print(user_time+" is equal to 23"+user_time[3]+user_time[4])

#This condition is dealing with times that are after 12:00 am but before 1:00 am. We want to make sure that this condition comes before the condition when the time is exactly 12:00 am because if the 12:00 am condition came first, then the computer would evaluate that as true and would never read this condition of code.
elif user_time[0]=="1" and user_time[1]=="2" and user_time[6]=="a" and user_time[3] is not"0":
  print(user_time+" is equal to 00"+user_time[3]+user_time[4])
#This is the condition for when the user puts in 12:00 am
elif user_time[0]=="1" and user_time[1]=="2" and user_time[6]=="a":
  print(user_time+" is equal to 24"+user_time[3]+user_time[4])
#This is the condition when the user puts in 12:00 pm
elif user_time[0]=="1" and user_time[1]=="2" and user_time[6]=="p":
  print(user_time+" is equal to 12"+user_time[3]+user_time[4])

else:
  print("Sorry, you did not enter a legitimate time.")