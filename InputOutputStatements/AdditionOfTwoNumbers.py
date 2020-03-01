#if we use explicit conversion functions like int() and pass value of a=2 and b=2.5 then we will get an error in addition
#Hence we are using eval() that will automatically do the proper type conversion before applying operation
x = input("Enter value of a:");
y = input('Enter value of b:');

print(eval(x)+ eval(y))

#Output
#Enter value of a:10
#Enter value of b:20
#30

print(int(x)+int(y)) #Will result in error if non-integer value is passed


#Enter value of a:10
#Enter value of b:3.5
#13.5  (eval() is perfectly working fine)
#Traceback (most recent call last):
#  File "d:/workspace/python-examples/InputOutputStatements/AdditionOfTwoNumbers.py", line 13, in <module>
#    print(int(x)+int(y))
#ValueError: invalid literal for int() with base 10: '3.5'