'''
This was learned from udemy course
What is string formatting?
String formatting is nothing is the way to represent non string elements in print statements and mostly the patterns how an user can use variable values inside print statements.
'''

age = 28

# We can not directly use the variable which is not of type sting in print statements or concat or manipulating statements
# print("My age is "+ age) 
# ERROR : TypeError: must be str, not int

'''
Converting the variable to string wont be the only solution when it comes to print statement
print ("My age is " str(age))
ERROR : SyntaxError: invalid syntax
'''

# We need to use comma to indicate that it will be followed by a vaiable to append to the print string.
print("My age is",age)
# but however this is the old way to use variable in print statement and the limitation is that we can not use more than one variable and at dynamic location in the print statement

'''
Old way to use multiple vaiables in print statement is as follows
'''
plain_number = 4
print("Number is %d, it's square is %d" %(plain_number,plain_number**2))
'''
This is the way we used to operate on variables in print staremetnest in 2.7 version
%d - integer
%f - float
%s - string

'''