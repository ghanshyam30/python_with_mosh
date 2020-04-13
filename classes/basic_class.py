# Basic class implementation

class BasicClass: # Class name should start with uppercase letter
    # The variable which is declared inside a class scope but outside of any method is termed as class variable
    variable1 = 0   # class variable 1

    # Any function inside a class definition is termed as Method

    # constructor method
    def __init__(self):
        first_name = None
        last_name = None
    
    #Instance method
    def set_name(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    def get_name(self):
        return (self.first_name+ " " + self.last_name)

new_person = BasicClass()
new_person.set_name("Ghana", "Bambale")
print(new_person.get_name())

