# Accepting user name as input
input_name = input("Please enter your good name:")

# Apply validation logic
# length of name < 3 => invalid
# length of name > 50 => invalid
# otherwise => valid

if len(input_name) < 3:
    print("name must be at least 3 characters!!")
elif len(input_name) > 50:
    print("name must be less than 50 charachters!!")
else:
    print("name looks good")

'''
Inputs:
1] Is
2] this is some practical session that you need to do on your own mosh can only guide you but the learning is dependent on your actions and our actions
3] Mosh
'''