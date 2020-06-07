# Learned from official documentation

def scopes():
    def do_local():
        spam = "Local spam"
    
    def do_non_local():
        nonlocal spam
        spam = "Non local spam"
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()    
    print(f"After local assignment:{spam}")
    do_non_local()
    print(f"After non local assignment:{spam}")
    do_global()
    print(f"After global assignment:{spam}")


    global new_global_variable 
    new_global_variable = "now this is global variable is from outer function"
    

scopes()
print(f"global scope:{spam}")

print(new_global_variable)