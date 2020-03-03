# In this we will use the  customer modules defined custommodulea and custommoduleb

import myfirstmodule as one
import mysecondmodule as two

one.name()
two.name()

print(one.fun_add(2,5)) #It will call function defined in custom  module
print(two.fun_mul(3,6))