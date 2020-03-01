# Dictionaries are like Map in java
# Key value paris separated by :
# Dictionaries have keys and values
# Keys are immutable and unique
# sample = {'a':10, 'b':20}
# 

d = {'Name': 'student', 'sub': ['Math','Eng'], 'Hobbies':('Dancing', 'Cricket')}
#length
print(len(d)) #3

#Getting element
print(d['Name']) #Student
print(d['sub']) #['Math', 'Eng']

#Adding an element
d['Class'] = 'VI'
print(len(d)) #4

#Print keys
print(d.keys()) #dict_keys(['Name', 'sub', 'Hobbies', 'Class'])
#Print values
print(d.values()) #dict_values(['student', ['Math', 'Eng'], ('Dancing', 'Cricket'), 'VI'])

#Membership
print('Class' in d) #True

#Delete a key
del(d['Class'])
print(d) #{'Name': 'student', 'sub': ['Math', 'Eng'], 'Hobbies': ('Dancing', 'Cricket')}
