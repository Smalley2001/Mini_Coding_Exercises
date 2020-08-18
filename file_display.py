# Assume that a file containing a series of integers is named numbers.txt and exists on the computer's disk. Write a program that displays all the numbers in the file. 

# Create a function that allows you to open files. To use open(), you have to declare the file and what type of form you want it. For this example, I created a file called numbers.txt and r means that it will be in a read only format. Then use readline which reads each line in the file. If readline ever equals "" (an empty string), it means readline is done reading the file. 


#If the file is not in the same folder, then you need the full extension inside of open().
def Main():
  numbers_file=open("numbers.txt", "r")
  line=numbers_file.readline()
  #Create a while loop for each line as long as readline doesn't equal to "" print(line). And then repeat readline. 
  while line != "":
    print(line)
    line=numbers_file.readline()

# Don't call forgett to call the function
Main()# Assume that a file containing a series of integers is named numbers.txt and exists on the computer's disk. Write a program that displays all the numbers in the file. 

# Create a function that allows you to open files. To use open(), you have to declare the file and what type of form you want it. For this example, I created a file called numbers.txt and r means that it will be in a read only format. Then use readline which reads each line in the file. If readline ever equals "" (an empty string), it means readline is done reading the file. 


#If the file is not in the same folder, then you need the full extension inside of open().
def Main():
  numbers_file=open("numbers.txt", "r")
  line=numbers_file.readline()
  #Create a while loop for each line as long as readline doesn't equal to "" print(line). And then repeat readline. 
  while line != "":
    print(line)
    line=numbers_file.readline()

# Don't call forgett to call the function
Main()