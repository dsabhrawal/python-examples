# Child class is able to access parent class methods and variables
# When one sub-child class is extending child which extends Parent class
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

class SubChild(Child):
    def __init__(self):
        super().__init__()
        print('SubChild Constructor')

    def displaySC(self):
        print('SubChild Display')
    

P = Parent()
P.displayP()
#P.displayC() #output error as Parent doesn't inherit child methods

C = Child()
C.displayC()  #Child class display
C.displayP()  #Inherited from parent

SC = SubChild()
SC.displayP()
SC.displayC()
SC.displaySC()

#Output
#Parent constructor
#Parent Display
#Parent constructor
#Child constructor
#Child Display
#Parent Display
#Parent constructor
#Child constructor
#SubChild Constructor
#Parent Display
#Child Display
#SubChild Display