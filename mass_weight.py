# Write a program that asks the user to enter an object's mass, and then calculate the weight. If the object weighs more than 500 newtons, display a message stating that it is too heavy. If the object is less than 100 pounds, display a message saying that is too light.

#For this problem, I decided to use a function for practice, which will print statements based on the conditions of an object's weight. To calculate weight, the user has to give a mass and gravity is rounded to 9.8 so weight = mass * 9.8.
def Weight():
  user_mass=float(input("What is the object's mass: "))
  user_weight= 9.8 * user_mass
  if user_weight>500:
    print("Your object weighs: " + format(user_weight,",.2f") + " newtons. The object is too heavy.")
  elif user_weight<100:
    print("Your object weighs: " + format(user_weight,",.2f") + " newtons. The object is too light.")
  else:
    print("Your object weighs: " + format(user_weight,",.2f") + " newtons. That is an acceptable weight.")

#Don't forget to call the function
Weight()