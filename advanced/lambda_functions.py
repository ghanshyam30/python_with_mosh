__author__ = "The Bad Coder"
from functools import reduce
# print(__author__)
'''
Syntax or Idea:
lambda <parameters separated by comma> : <operation on parameters>,<input sequence>
And this lambda function we can use with Map,Filter,Reduce for different purposes
'''

def implement_lambda_function():
    """
    If we want to deal with some sequence type with some pattern in it, then it is better to use lambda functions rather than
    for loop or any kind of loop which is slower and non pythonic way to do the coding.
    Tip : User cannot directly use the lambda result first store it in filter or map data structure and then convert it to
    a list or any sequence basic data type and iterate over it using any loop
    """
    '''
    Filter: Filter will return only those elements from given sequence who satisfyies criteria
    Problem : Find the items with some price criteria
    '''
    price = 1
    result_set = filter(lambda fruit:fruit[price]>40, fruits)
    
    # Checking the type of result 
    print(type(result_set))

    # Checking the functionality of filter object
    print("Possible operations:",(type(result_set)).__dict__)

    # Checking what result has got like it is an object or it is value
    print("Result set=",result_set)

    # We can iterate over the filter / map object like any other sequence
    # REMOVE print(fruit[0] for fruit in result_set)
    print("Filtered fruits from given list are:")
    fruit_name = 0                          
    for filtered_fruit in list(result_set):                     #converting the filter object to list
        print(filtered_fruit[fruit_name])


# To access docstring we need to call the fuction without paranthesis or parameters
print("Program description: Lambda Functions\n",implement_lambda_function.__doc__)

# given sequence
fruits = [("Mango", 100), ("Apple",50),("Banana",10)]       #list of tuples having item name and item price each

# Call the function
implement_lambda_function()


#############################################################################
#                               MAPS                                        #
#############################################################################
'''
Map performs given operation on the sequence and returns the result sequence
Problem 2: With the same list we want to deal with only prices
'''
price = 1                       # tuple index to operate on for prices
prices_data = map(lambda fruit_price: fruit_price[price], fruits)    # lambda function applied

# Checking the functionality of filter object
print("Possible operations:",(type(prices_data)).__dict__)

# convert the result to list and print 
print("The captured prices from the given data are as follows:")
for price_item in list(prices_data):
    print(price_item)



##########################################################################
#                            Reduce                                      #
##########################################################################
'''
Reduce is a special function where it operates on 2 elements, 1st element being result of operation of initial 2 elements in the sequence and 2nd element is thrid item from given sequence.
Reduce does this till the sequence is fully processed.
Problem: find the sum of elements in the list
'''
some_list = [1,2,3,4,5]
reduce_result = reduce(lambda x,y:x+y,some_list)
print("Original List:",some_list)
print("Reduce sum=",reduce_result)

##########################################################################
#                           Output                                       #
##########################################################################
'''
Program description: Lambda Functions
 
    If we want to deal with some sequence type with some pattern in it it is better to use lambda functions rather than
    for loop or any kind of loop which is slower and mnon pythonic way to do the coding.
    Tip : User can not directly use the lambda result first store it in filter or map data structure and then convert it to
    a list or any sequence basic data type and iterate over it using any loop
    
<class 'filter'>
Possible operations: {'__getattribute__': <slot wrapper '__getattribute__' of 'filter' objects>, '__iter__': <slot wrapper '__iter__' of 'filter' objects>, '__next__': <slot wrapper '__next__' of 'filter' objects>, '__new__': <built-in method __new__ of type object at 0x9c1240>, '__reduce__': <method '__reduce__' of 'filter' objects>, '__doc__': 'filter(function or None, iterable) --> filter object\n\nReturn an iterator yielding those items of iterable for which function(item)\nis true. If function is None, return the items that are true.'}
Result set= <filter object at 0x7f0dc96bd128>
Filtered fruits from given list are:
Mango
Apple
The captured prices from the given data are as follows:
100
50
10
'''
