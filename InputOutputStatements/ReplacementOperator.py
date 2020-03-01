#For replacement of the actual value str.format() is used

a = 5
b = 10

print('Sum of {} and {} is {}'.format(a,b,a+b))
print('Sum of {0} and {1} is {2}'.format(a,b,a+b)) #Parameterized input

print()
print('Sum of {num1} and {num2} is {num3}'.format(num1=a,num2=b,num3=(a+b)))


#Output
#Sum of 5 and 10 is 15