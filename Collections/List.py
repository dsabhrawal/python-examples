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
#modify list
s[0] = 'Loving'
s[1] = 'The'
print(s) #['Loving', 'The', 'python']
#slicing the list
print(s[0:2]) #['Loving', 'The']
print('deep' in s) #False
print('python' in s) #True

#Sorting
numbers = [10,40,4,6,7,2,50]
numbers2 = numbers.copy()
numbers2.sort() 
print(numbers) #output: [10, 40, 4, 6, 7, 2, 50]
print(f'sorted numbers! {numbers2}') #output: [2, 4, 6, 7, 10, 40, 50]

#List Iteration
for i in s:
    print(i)

for i in range(len(s)):
    print(i, s[i]) #Print value with index

#2D List
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
#output: 2
#-- Print whole 2D List
for row in matrix:
    for item in row:
        print(f'item {item}')
#output:
'''
item 1
item 2
item 3
item 4
item 5
item 6
item 7
item 8
item 9
'''

#Remove duplicates from the list
numbers = [3,4,5,3,4,7,8,8,1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
#output: [3, 4, 5, 7, 8, 1]