
w = 9 #Default Number representation base 10 decimal
x = 0b1010 #Binary number base 2
y = 0o1247 #Octal Number base 8
z = 0xa43d #Hexadecimal number base 16

print(w); #9
print(type(w)); #<class 'int'>

print(x); #10
print(type(x)); #<class 'int'>

print(y); #679
print(type(y)); #<class 'int'>


print(z); #42045
print(type(z)); #<class 'int'>

#decimal to hex conversion
print(hex(w)); #0x9
#decimal to octal
print(oct(w)); #0o11
print(bin(w)); #0b1001

#Floating point number
a = 10.25
print(a) #10.25
print(type(a)) #<class 'float'>

#Floating point is upto 16 digit precision

#Complex Numbers
p = 2 + 3j
print(p.real) #print real value #2.0
print(p.imag) #print imaginary value #3.0