# Some of the built in modules are Math, Random, Time, Threading

#Print members of a module

import math

print(dir(math))  #List of members in math module
for i in dir(math):
    print(i)

#Use alias to import
import math as m

print(m.pi) #Need qualifier to access members

#Use selective import
# No need to use qualifier
# Module member becomes part of the code
from math import pi,sqrt as s

print(s(4)) # 2.0

# Import all from a module
from math import *
print(factorial(5)) #120