
s = "Hello Python"  #Singline string
print(s)
print(type(s))


#Multiple line strings
#Mainly used for comments

s = '''This is a 
        Multiple line
        string'''
print(s)

s = '''It is 'a good' "example" '''

print(s)

#Next line
print('\n \n')

#String Format for left/right/center justified
s = 'Hello Python'
#Left Justified
s1 = format(s,'-<20')
print(s1)

# Right Justified
s1 = format(s,'->20')
print(s1)

#center Justified
s1 = format(s, '-^20')
print(s1)

#String Functions
print('\n\n')

s = 'Hellopython'
print(len(s))
print(max(s)) #based on ascci value
print(min(s)) #based on ascii value

#String indexing
print(s[1]) #first character
print(s[-1]) #last character

#String slicing
print(s[0:4])
print(s[::2]) #every second character select

#String functions
print(s.index('h'))
print('\n')
print(s.count('h'))

