# In physics, an object that is in motion has kinetic energy. Write a function named kinetic_energy that accepts an object's mass (in kilograms) and velocity ( in meters per second) as arguments. The function should return the amount of kinetic energy that the object has. Write a program that asks the user to enter values for mass and velocity, and then calls the kinetic_energy function to get the object's kinetic energy. 

def kinetic_energy(mass,velocity):
  energy= 0.5 *mass * (velocity **2)
  return energy

def Main():
  mass= float(input("What is the total mass in kilograms: "))
  velocity= float(input("What is the total velocity in meters per second: "))
  k_energy= kinetic_energy(mass,velocity)
  print("An object with a mass of: " + format(mass, ",.2f") + " kilograms and a velocity of: " + format(velocity,",.2f") + " meters per second. Has a kinetic energy of: " + format(k_energy, ",.2f") + " Joules.")

Main()