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
