# List in py is mutable collection
# Concatinaton of list
# list is zero indexed
# Can hold multiple data types
# List supports negative indexing

l = ['Jack', 1000, 20.3, True]
print(l) #['Jack', 1000, 20.3, True]

#l[0] == l[-4] (Negative indexing last element is indexed -1)

print(l[0], l[-4]) #Jack Jack
#Concatination
s = l + ['John',20000]
print(s) #['Jack', 1000, 20.3, True, 'John', 20000]

#append (single element)
l.append(30.5)
print(l) #['Jack', 1000, 20.3, True, 30.5]

#append (multiple elements)
l.extend([11,'ok'])
print(l) #['Jack', 1000, 20.3, True, 30.5, 11, 'ok']

#deleting with del
del(l[1]) #Deleting element at index 1
print(l) #['Jack', 20.3, True, 30.5, 11, 'ok']

#sum() of all elements
q = [10,20,30]
print(sum(q)) #60
#sort()
q.sort() #Default ascending order
print(q) #[10, 20, 30]
#reverse()
q.reverse()
print(q) #[30, 20, 10]
#min()
print(min(q)) #10
#max()
print(max(q)) #30
#String to list
s = 'This is python'.split()
print(s) #['This', 'is', 'python']
#len() lenght of list
print(len(s)) #3
