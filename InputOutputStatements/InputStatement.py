# Type of value input function returns in always Str
#input()

x = input('Enter value: ')

print(x)
print(type(x))

#Enter value: 12
#12
#<class 'str'>

#Enter value: Hello
#Hello
#<class 'str'>

## Reading Multiple values in a single statement

x,y = input('Enter values: ').split()  #Space is default delimiter here

print(x)
print(y)

#Enter values: 10 12
#10
#12

x,y = input('Enter Values: ').split(',')  #To get the comma delimited input 

print(x)
print(y)

#Enter Values: 12,12
#12
#12