# Always latest version of the method is executed

# Same name method in same class

class Test:
    def display(self):
        print('Display')
    
    def display(self,x):
        print('Display ',x)

t = Test()
#t.display()  # Error, because display(self,x) is the latest definition and that expects on argument to be paased
t.display(10) # Display 10

# Same name method in parent and child class

class A:
    def display(self):
        print('Display of A')
    
class B(A):
    def display(self,x):
        print('Display Of B with vlaue ',x)

b = B()
#b.display()  # Error
b.display(10)  #Display Of B with vlaue  10

# Every class has a method mro which specifies the Method Resolution Order
print(B.mro())
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]