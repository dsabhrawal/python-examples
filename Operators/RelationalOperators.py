#<, <=, >=, >

print(2 < 3) #True
print(4 > 1) #Falsle

#In String the ascii value is compared

a = 'aaa';
b = 'aad';

print(a > b) #False
print(a < b) #True

#chaining of relational operators

p,q,r,s = 10,20,30,40

print(p < q > r < s) #False (Individual expression evaluation is followed by AND)
print(p < q < r < s) #True