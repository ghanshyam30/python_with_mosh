# VARIABLES

price = 10

rating = 4.9

course_name = 'Python for Beginners'

is_published = True

# To print the actual value variable holds
print(price)

# To print types of above variables
print(type(price))

print(type(rating))

print(type(course_name))

print(type(is_published))

# Receiving Input and assigning it to a variable
# Note:The input() function always returns data as a string. So, we’re converting the result into an integer by calling the built-in int() function. 
# input function can hold an informative message for the end user so that the user can read it and provide input accordingly
birth_year = input("Enter your birth year:") 
print("Type of the birth_year variable:",type(birth_year))
# Converting input to desired type
birth_year = int(input("Enter your birth year:"))
print("Type of the birth_year variable:",type(birth_year))
