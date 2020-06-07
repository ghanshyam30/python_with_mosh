# Basic class implementation

class BasicClass: # Class name should start with uppercase letter
    # The variable which is declared inside a class scope but outside of any method is termed as class variable
    variable1 = 0   # class variable 1

    # Any function inside a class definition is termed as Method

    # constructor method - A constructor should initianlize the object attributes with default values
    def __init__(self,fname,lname):             # fname and lname are termed as parameters and not the arguments which are real values
        self.first_name = fname                 #self keyword is needed to access the respective object of the class.
        self.last_name = lname

    #Instance method
    def get_name(self):
        return (self.first_name+ " " + self.last_name)

# An object creation - should have arguments to be passed to class constructor
new_person = BasicClass("Tom", "Cruise")             # Tom and Cruise are 2 arguments we are passing to the constructor
print(new_person.get_name())

############################################
# OUTPUT:
# Tom Cruise
############################################