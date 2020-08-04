# Assume that hot dogs come in packages 10, and hot dog buns come in packages of 8. Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the amount of leftovers and the number of hot dogs each person will be given. The program should display the following details:

#The minimum number of packages of hot dogs required
#The minimum number of packages of hot dog buns required 
#The number of hot dogs that will be left over
#The number of hot dog buns that will be left over
hot_dogs_per_package= 10
hot_dog_buns_per_package=8

People_number=int(input("How many people will be attending the cookout: "))
hot_dogs_per_person= int(input("How many hot dogs will each of the " + str(People_number) + " people receive: "))

number_of_hot_dogs_needed= hot_dogs_per_person * People_number

Hot_dog_packages_needed= number_of_hot_dogs_needed/hot_dog_buns_per_package

buns_packages_needed= number_of_hot_dogs_needed/hot_dog_buns_per_package

hot_dog_packages_remainder= number_of_hot_dogs_needed % hot_dogs_per_package

hot_dog_buns_packages_remainder= number_of_hot_dogs_needed % hot_dog_buns_per_package

if hot_dog_packages_remainder>0:
  minimum_hot_dog_packages_required=int(Hot_dog_packages_needed +1)
else:
  minimum_hot_dog_packages_required=Hot_dog_packages_needed

if hot_dog_buns_packages_remainder>0:
  minimum_hot_dog_buns_packages_required= int(buns_packages_needed + 1)
else:
  minimum_hot_dog_buns_packages_required=buns_packages_needed

left_over_hot_dogs= int(minimum_hot_dog_packages_required- Hot_dog_packages_needed)

left_over_hot_dog_buns= int(minimum_hot_dog_buns_packages_required - buns_packages_needed)

print("Minimum number of packages of hot dogs required: " + str(minimum_hot_dog_packages_required) + " \nMinimum number of packages of hot dogs buns required: " + str(minimum_hot_dog_buns_packages_required) + " \nHot dogs left over: " + str(left_over_hot_dogs) + " \nThe number of hot dog buns that will be left over: " + str(left_over_hot_dog_buns) )