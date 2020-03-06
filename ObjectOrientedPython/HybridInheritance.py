# Class B and C extends A (Hierarchical Inheritance)
# Class D extends B and C (Multiple Inheritance)

class A:
    def displayA(self):
        print('A Display')

class B(A):   
    def displayB(self):
        print('B Display')

class C(A): 
    def displayC(self):
        print('C Display')

class D(B,C):
    def displayD(self):
        print('D Display')

# We can have all the methods of A,B,C and D visible with D's instance
d = D()
d.displayA()
d.displayB()
d.displayC()
d.displayD()

#Output:
# A Display
# B Display
# C Display
# D Display