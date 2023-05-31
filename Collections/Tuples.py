# Tuples are ordered sequence
# Immutable
# tuples can have same or mix data type
# (1,'a',1.6)

x = (1,'a',1.5)
print(x)
y = (10,20,30)
#we can perform len() min() max() sum() operations similar to list
print(len(x)) #3
print(min(y)) #10
print(max(y)) #30
print(sum(y)) #60

#slicing
print(y[0:2]) #(10,20)

#Concatination
z = x + y
print(z) #(1, 'a', 1.5, 10, 20, 30)

#Copy topule
d = z[:]
print(d) #(1, 'a', 1.5, 10, 20, 30)

#Membership
print(1 in d) #True

#Iteration
for i in d:
    print(i)

#Nested List and Tuples
l = [100, ['a', 'b', 'c'], 'paas']
print(l)
#Print nested elements
print(l[1][0]) #a
print(l[1][1]) #b

g = [10,('a','b','c'), 'fail'] #Tuple inside list

print(type(g[1])) #<cjass 'tuple'>

#unpacking 
numbers = (1,2,3)
x,y,z = numbers 
print(x)
print(y)
print(z)
#output:
'''
1
2
3
'''