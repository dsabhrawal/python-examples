# Lambda functions are the annonymous functions
# Lambda functions have no name
# Created for one time use or instant use
# Do not have return statement

#Normal Function
def ex_add(a):
    return a+a #10 

print(ex_add(5))

#Lambda Function
x = lambda a: a+a
print(x(5)) #10 using lambda