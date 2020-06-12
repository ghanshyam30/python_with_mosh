__author__ = 'The Bad Coder'
'''
When an exception occrs, the Python interpreter stops the current process and 
passes it to the calling process untill it is handled.
It the exception is not at all handled the program will crash

The  critical operation which can raise an exceptuon is placed inside
the try clause. The code that handles the exception is written in the 
except clause
'''
'''
Probelm statement :
Declare the class which will have a fucntion which will take some
input from the user and does some processing to give output
Lets implement the try for input dict_values.
'''

# Declare the class
class ExceptionHandling:
    def fill_form(self, first_name, last_name, age, mobile_no):
        self.person_first_name = first_name
        self.person_last_name = last_name
        self.person_age = age
        self.mobile_no = mobile_no
    
    def check_voting_rights(self):
        try:
            if self.person_age-18 > 0 :
                print(f"{self.person_first_name} has the voting rights")
            else:
                print(f"{self.person_first_name} doesn't have voting rights")
        except:
            print("Please check the age, there seems some SPAM data")


naruto = ExceptionHandling()
def fill_form():
    fname_input = input("First Name: ")
    lname_input = input("Last Name : ")
    mobile_no_input = input("Mobile No : ")
    # converting age into integer wont go into the exception
    # not converting the age to int will land the code int the exception
    age_input   = int(input("Age       : "))
    naruto.fill_form(fname_input, lname_input, age_input, mobile_no_input)
    naruto.check_voting_rights()

fill_form()


######################## OUTPUT ###########################
# Whend exception is handled
First Name: Naruto
Last Name : Uzumaki
Mobile No  : 9999999999
Age       : 14
Please check the age, there seems some SPAM data

#When age is converted to integer but age < 18
First Name: Naruto
Last Name : Uzumaki
Mobile No : 9999999999
Age       : 14
Naruto doesn't have voting rights

# When age is converted to int and age is > 18
First Name: Etachi
Last Name : Uchiha
Mobile No : 8888888888
Age       : 21
Etachi has the voting rights