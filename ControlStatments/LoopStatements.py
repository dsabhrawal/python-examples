# loop statements in Python


#Print numbers 1 to 10

x = 1
while x<=10:
    print(x)
    x +=1
print('End of Program!')


#For loop

for char in 'John':
    print(char) #Each character is printed

print()
print()

a=range(10)
for i in a:
    print(i)  #Prints number 0-9
print()

#Prints 10 to 1 numbers
k = range(10,0,-1)
for z in k: 
    print(z)

print()
print()
#Break and continue

#Find first odd number in the given list
list = [10,50,11,12,17]
for i in list:
    if(i%2 == 0):
        continue
    print(i)
    break

#Result: 11

#Nested Loops
for x in range(4):
    for y in range(3):
        print(f'({x}),({y})')
        
#Output
'''
(0),(0)
(0),(1)
(0),(2)
(1),(0)
(1),(1)
(1),(2)
(2),(0)
(2),(1)
(2),(2)
(3),(0)
(3),(1)
(3),(2)
'''