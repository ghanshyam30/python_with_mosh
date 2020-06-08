__author__ = "The Bad Coder"

'''
Polymorphism is an ability to use common interface for multimple fors/ datatypes
In python we can not have 2 methods with same name in same class but if we have them
in 2 different classes we can declare 1 interface and provide an object as parameter
and access the method using this object in the interface.
'''


class Parrot:
    def fly(self):
        print("Parrot can fly.")

    def swim(self):
        print("Parrot can't swim.")

class Penguin:
    def fly(self):
        print("Penguin can't fly.")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def test_fly(bird):     # taking objects as parameter
    bird.fly()          # accessing same method from any different object having the method

# Create objects
blu = Parrot()
peggy = Penguin()

# Use same interface to call a method for different objects of different classes
test_fly(blu)
test_fly(peggy)

