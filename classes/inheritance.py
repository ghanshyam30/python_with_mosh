# Inheritace is one of the important Object oriented programming concept.
# Inheritance allows a class (derivied class) to inherit properties and features of the other class(parent or base class).
# Why inheritance - it leverages coder reusability, transition and readability, realworld relationship

class Employee:
    regular_hike = 15           # Hike in percentage
    def __init__(self,fname, lname):
        self.first_name= fname
        self.last_name= lname
        self.salary = 5000

    def set_salary(self):
        self.salary = 5000 * (1+(Employee.regular_hike/100))

    def set_contact(self,contact):
        self.contact = contact
    
    def get_info(self):
        print(f"Name= {self.first_name} {self.last_name}")
        print(f"Salary= {self.salary}")
        print(f"Contact= {self.contact}")

class Developer(Employee):
    dev_raise = 20
    def __init__(self,fname,lname,role):
        super().__init__(fname,lname)
        self.role = role
    def set_salary(self):
        #print("This is dev salary here..")
        self.salary = 5000 * (1+(Developer.dev_raise/100))
        # print(self.salary)
    def get_info(self):
        print(f"Name= {self.first_name} {self.last_name}")
        print(f"Salary= {self.salary}")
        print(f"Contact= {self.contact}")


emp_tom = Developer("Tom","Cruise","Developer")
emp_tom.set_contact(9900000001)
emp_tom.set_salary()
emp_tom.get_info()


emp_regular = Employee("John", "Smith")
emp_regular.set_contact(9900000002)
emp_regular.set_salary()
emp_regular.get_info()