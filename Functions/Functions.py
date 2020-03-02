# Function is a piece of code of sequence of statements
# Function is executed when it is called
# Function works strictly with indentation
# Function may or may not return a value
# Function can have zero or more arguments passed
# Function has to be defined before using it
# Example:
#    def addition(a,b):
#        return a+b
#
# Calling function addition(2,4)
# Multiple parameters can be passed. 
# Example: def my_fun(*a)
# my_fun(1,2) or my_fun(3,4,5,6)

# Function without a body is defined as 
def do_nothing():
     pass

do_nothing() # Calling function

# Print sum of two numbers
def sum(a,b):
    return a+b

x = sum(2,3) #Calling function and assign value to x
print(x)  #Prints 5

#Multiple Parameters
def do_multiply(*a):
    result = 1
    for i in a:  
        print(type(a)) #prints <class 'tuple'> a is a tuple here
        result *=i
    return result

print(do_multiply(2,4)) #Prints 8
print(do_multiply(3,'Hi')) #Prints HiHiHi


# Keyword argument to paas the values 

def ex_keyword_arg(a,b,c):
    print('Value of a:',a)
    print('Value of b:',b)
    print('Value of c:',c)
    print('Sum of abc: ', (a+b+c))

ex_keyword_arg(2,4,5) #a=2, b=4, c=5 and sum is 11
ex_keyword_arg(2,c=4,b=5) #a=2, b=5 , c=4 and sum is 11

# Function with default argument values
def ex_default_arg(a,b=2,c=6):
    print('Value of a:',a)
    print('Value of b:',b)
    print('Value of c:',c)
    print('Sum of abc: ', (a+b+c))  

ex_default_arg(2) # sum of abc: 10
ex_default_arg(2,5) # sum of abc: 13 (5 is assigned to b)