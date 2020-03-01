#Following are the operators supported
# + Addition
# - Subration
# * Multiplication
# / Division
# % Modulus 
# // Integer Division
# ** Exponential
# 

#If any of operand is float the result is float
print(3+2)  #prints 5
print(3-2)  #prints 1
print(3*2)  #prints 6
print(2.5+2)  #Prints 4.5 (float)

#In division result is always float irrespective of Operand
print(10/2)  #Prints 5.0

#In Modulus if both the operands are Integer the result is Integer and If one operand is float the result is float
print(5%2)  #Prints 1
print(14.75%4) #prints 2.75 

#In Exponential if both the operands are Integer the result is Integer and If one operand is float the result is float
print(3.5**2)  #Prints 12.25
print(3**3)  #Prints 27

#Integer division is also called as floor division. First performs the normal division and then applies floor() to result
print(10.5//2) #Prints 5.0
print(-5//2)  #Prints -3

#Arithmetic Operations on Strings
print('2'+'3') #Prints 23
print('abc'+str(2+3))  #Prints abc5

print(3*'Hello')  #Prints HelloHelloHello
print(3*True)  #Prints 3 (True converted to 1)

#Arithmetic Operations on Complex Numbers
e = 2+3j
f = 4-6j

print(e+f)  #Prints (6-3j)
print(e*f)  #Prints (26+0j)
print(e-f)  #Prints (-2+9j)
