#and , or , not  (Str, bool ,int)

a = True
b = False 

print(a and a) #True
print(a and b) #False
print(b and b) #False
print(a or b)  #True
print(not b)   #True

p = 10 
q = 20
print(p and q) #20 (as p is considered True and for 'and' operator the second operand will be checked to get final result)
print(p or q)  #10 (as p is considered True therefore second operand will not be checked for 'or' operation)
print(0 and p) #0 (as 0 is considered as False and for 'and' operator if first operand is False second is not considered)
print(0 or p) #10 (as 0 is considered False second operand will be checked to get final result)

x = ''
y = ' '
z = 'can'

print(not x) #True (Empty string is considered false)
print(not y) #False (As string contains space)
print(not z) #False (As string is not empty)
print('ab' or 'abc')