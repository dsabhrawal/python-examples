# When one base class is extending one parent class

# Child class is able to access parent class methods and variables

class Parent:
    def __init__(self):
        super().__init__()
        print('Parent constructor')
    
    def displayP(self):
        print('Parent Display')

class Child(Parent):  #Inherited from the Parent class
    def __init__(self):
        super().__init__()
        print('Child constructor')
    
    def displayC(self):
        print('Child Display')
    

P = Parent()
P.displayP()
#P.displayC() #output error as Parent doesn't inherit child methods

C = Child()
C.displayC()  #Child class display
C.displayP()  #Inherited from parent
