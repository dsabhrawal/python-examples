# When two child classes extends same base class
# Child class can inherit methods for parent but not the other child classes

class A:
    def displayA(self):
        print('A Display')

class B(A):   #B extends A
    def displayB(self):
        print('B Display')

class C(A):   #C extends A
    def displayC(self):
        print('C Display')


a = A()
a.displayA() # A Display

b = B()
b.displayA() # A Display
b.displayB()  # B Display
#b.displayC()  #Error

c = C()
c.displayA() # A Display
c.displayC() # C Display
#c.displayB()  # Error
