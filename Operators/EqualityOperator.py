# == , != (Int, float, str, bool)

x,y=6,7
p=6

print(x == y) #False
print(p == x) #True

print(p == 6.0) #True

print('Hello' == 'Hello') #True

#Chaining
print(10 == 20 == 6 == 3) #False
print(1 == 1 == 1 < 2)    #True
print(1 !=2 < 3 > 1) #True