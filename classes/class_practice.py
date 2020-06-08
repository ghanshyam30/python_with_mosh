__author__ = "The Bad Coder"

# Create a basic class which we can turn into a parent class later for inheritance
class Dog:
    species = "mammal"      # class variable, ultimate example

    # Initializer/constructior with instance attributes/variables
    def __init__(self, name, age):
        """ constructor can set name and age of a dog."""
        self.dog_name = name
        self.dog_age  = age
        print(f"{self.dog_name} is {self.dog_age} years old.")

    # Behavior / Functionss
    def speak(self, sound):
        print(f"{self.dog_name} says {sound}.")

    
    
# Instantiate the object of Dog class
mikey = Dog('Mikey', 4)
mikey.speak("Gruff Gruff")
# read class vairable
print(f"Species that {mikey.dog_name} belongs to is {mikey.species}")

# Exceptional behavior when we tried to change the class variable for one instance it changed.
mikey.species = "animal"
print(f"Now we have changed {mikey.dog_name}'s species to {mikey.species}")


###############
# INHERITANCE #
###############
class RusselTerrier(Dog):
    def run(self, speed):
        self.dog_speed = speed
        print(f"{self.dog_name} runs with {self.dog_speed} speed.")
    
    def set_price(self, sell_price):
        # Encapsulation
        # private variable can not be updated by object alone.
        # along with you need to call the method and provide parameter to update private var.
        self.__sell_price = sell_price      # __sell_price is a private variable 
    
    def get_price(self):
        print(f"Selling price of {self.dog_name} is {self.__sell_price}")

class BullDog(Dog):
    def run(self, speed):
        self.dog_speed = speed
        print(f"{self.dog_name} runs with {self.dog_speed} speed.")
    
    def set_price(self, sell_price):
        self.__sell_price = sell_price
    
    def get_price(self):
        print(f"Selling price of {self.dog_name} is {self.__sell_price}")

# Creating object of 1 child class but it needs to satisfy attributes required for parent class's constructor
tommy = RusselTerrier("Tommy",5)
tommy.run("fast")
tommy.set_price(4000)           # set the price for dog
tommy.get_price()               # get the price of dog

#Doubt : why this statement does'nt produce an error?
tommy.__sell_price = 5000       # try to set the private variable
tommy.get_price()               # check again if setting private variable has any effect

# Creating object of 2nd clild class b
rusty = BullDog("Rusty", 2)
rusty.run("slow")
########################### OUTPUT ##################################
'''
SIMPLE CLASS-
---------------------------
Mikey is 4 years old.
Mikey says Gruff Gruff.
Species that Mikey belongs to is mammal
Now we have changed Mikey's species to animal

INHERITANCE:
----------------------------
Tommy is 5 years old.
Tommy runs with fast speed.
Rusty is 2 years old.
Rusty runs with slow speed.
'''