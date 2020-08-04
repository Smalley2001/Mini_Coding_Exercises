# This is an activity just to showcase how to showcase class Inheritance. I created a class called Car() which has attributes including brakes, wheels, color, etc. This is known as the parent class. These attributes will be shared with any instance of this class unless I specifically change it in an inherited class such as Lamborghini (the child class)

class Car():
  has_brakes= True
  has_wheels=True
  color= ""
  name=""
  max_speed= 100

 # These are child classes which have their own specific attributes that aren't necessarily the same as every instance of the class Car().
class Lamborghini(Car):
  max_speed=225
  convertible=True
  color="Red"

class Bugatti(Car):
  max_speed=300
  color="Black"

#With these classes, I can create variables using the class atributtes and determine the features I want to detail on my variable that I named my_car. Unless specify the character's attributes, it will have the same attributes as the class created.
my_car=Car()
my_car.name="Dorian"
my_car.max_speed=160
print(my_car.max_speed)

my_bugatti=Bugatti()
my_bugatti.name="Karl"
my_bugatti.color="Blue"
print(my_bugatti.color)

my_lamborghini=Lamborghini()
my_lamborghini.name="Jasmine"
my_lamborghini.color="Green"
#Even though, I didn't specify max_speed, it referenced the class max speed. 
print(my_lamborghini.max_speed)

#I made a separate class named Spongebob(). In this example, I am using __init__ which is the instantation operatation that allows me to give objects of this class a specfic description without having to consistently create inherited classes. For functions regarding classes, you must use self, to connect all activity to the class. I then created instances of this class in different variables and assigned them different values.
class Spongebob():

    def __init__(self,name):
      self.name=name
      self.attitudes=[]
  
    def add_attitude(self,attitude):
      self.attitudes.append(attitude)

sponge= Spongebob("Spongebob Squarepants")
squid= Spongebob("Squidward Tentacles")
star= Spongebob("Patrick Star")
sponge.add_attitude("Happy")
squid.add_attitude("Mean")
star.add_attitude("Dumb")
print(sponge.attitudes)
print(star.attitudes)
print(squid.attitudes)
