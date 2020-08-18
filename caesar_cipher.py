#This is a porgram that should take a given string of letters and return the next string in the alpahabet.

#For example, if the user puts in ("abc",1) then the output should be "bcd"

#The string does not have to be in order.

#For example, if the user puts in ("dxz",1) then the output should be "eya".




#Create a function that takes a string as an argument, and takes the number of indices to skip to.

#Store the alphabet as a string in a variable and a new variable that will store an empty string that will take the new letters after iteration.

#Create a for loop that iterates through the input string, called word in this case. 

#Use the find operation which will go through a string and identify what index the letter is at. So the variable index will return a number. Add n to index so we know what the overall index we are searching for is.

#We must recognize that if index is greater than 25, which is the last index in the alaphabet, then we will get an error so we can use the modulus in a conditional statement to ensure that the program resorts back to the start of the alphabet.

#Create a variable that will store the value of the index and add that to the variable holding the empty string. Print results
def rot_n(word, n):
	alphabet="abcdefghijk"
	new_string=""
	for letter in word:
		index=alphabet.find(letter)+n
		if index>25:
			index=index%26
		letter= alphabet[index]
		new_string+= letter
	print(new_string)

rot_n("abc",8)