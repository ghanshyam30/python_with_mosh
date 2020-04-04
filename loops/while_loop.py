'''
We always need to take care of 3 things while inplementing the loops
1. An interator for looping
2. A condition to exit from the loop
3. incrementer or decrementer of the iterator
'''

'''
command line application-
> start
o/p - Car started.
> stop
o/p - Car stopped.
> help
o/p -
start - To start the car
stop - To stop the car
quit - To exit from application
> anything else
o/p - I don't understand that 
'''
command=input(">").lower()
start_flag = False
while command!='quit':
    if command == 'start':
        if start_flag:
            print("Car is already started.")
        else:
            print("Car started.")
            start_flag = True
    elif command =='stop':
        if not start_flag:
            print("Car is already stopped")
        else:
            print("Car stopped.")
            start_flag = False
    elif command == 'help':
        print("""
start - To start the car
stop - To stop the car
quit - To exit from application
        """)
    else:
        print("I don't understand that")
    command=input(">").lower()