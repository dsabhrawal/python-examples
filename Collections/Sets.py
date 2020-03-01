# Unordered  elements
# Unique elements
# same of mix data type
# {'a', 1 , 2.5}

#Removing duplicates from a list
l = [10,20,10,30,50,30]
print(l)
s = set(l) #[10, 20, 10, 30, 50, 30]
print(s)  #{10, 20, 50, 30}

#len
print(len(s)) #4

#add
s.add(60)

#remove
s.remove(10)

print(s) #{50, 20, 60, 30}

#membership
print(50 in s) #True

#Intersection of two sets
s1 = {10,50,20,80}
print(s1.intersection(s)) #{50, 20}

#Union
print(s.union(s1)) #{10, 80, 50, 20, 60, 30}

s2 = {10,'a',10,'b',2.5}

#Duplicates are automatically removed
#Order is decided by python
print(s2) #{'a', 10, 2.5, 'b'}

#Iteration
for i in s2:
    print(i)

s3 = {10,20}
s4 = {10,20}
s5 = {10,30,40}
print(s3 is s4) #False
print(s3 == s4) #True 

#Set subtraction
s6 = s5 - s4
print(s6) #{40, 30}