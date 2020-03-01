#This examples talks about int() float() bool() str() complex() eval() conversion functions 

#int()
x = 10.5
print(int(x))  #prints 10

#float()
y = 7
print(float(y))   #prints 7.0

#bool()
print(bool(y))  #print True
print(bool(x)) #print True
print(bool(0)) #Print False

#str()
print(str('10.5555'))
print(str(x))

#complex()
print(complex(2))  #prints (2+0j)
print(complex(2,1)) #prints (2+1j)
print(complex(x))  #prints (10.5+0j)
print(complex(10.5,4))  #prints (10.5+4j)
print(complex(0b1001,0o34)) #prints (9+28j) Converts to decimal 


#eval()
p = eval('10')
print(p)
print(type(p))
#10
#<class 'int'>

q = eval('10.5')
print(q)
print(type(q))

#10.5
#<class 'float'>

