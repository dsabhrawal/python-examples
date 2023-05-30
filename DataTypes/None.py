x = 10

print(type(x)) #<class 'int'>

x = None

print(type(x)) #<class 'NoneType'>


#All variables points to single locaiton of None value in Memory
x = None
y = None
z = None

print(id(x))
print(id(y))
print(id(z))

#Answer
#139932057840128
#139932057840128
#139932057840128