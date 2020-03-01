
w = 9 #Default Number representation base 10 decimal
x = 0b1010 #Binary number base 2
y = 0o1247 #Octal Number base 8
z = 0xa43d #Hexadecimal number base 16

print(w);
print(type(w));

print(x);
print(type(x));

print(y);
print(type(y));


print(z);
print(type(z));

#decimal to hex conversion
print(hex(w));
#decimal to octal
print(oct(w));
print(bin(w));

#Floating point number
a = 10.25
print(a)
print(type(a))

#Floating point is upto 16 digit precision

#Complex Numbers
p = 2 + 3j
print(p.real) #print real value
print(p.imag) #print imaginary value