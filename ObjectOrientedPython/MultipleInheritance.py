# When one child class inherits more than one parent class

class A:
    def displayA(self):
        print('A Display')
    
    def look(self):
        print('A Looking')

class B:   
    def displayB(self):
        print('B Display')
    
    def look(self):
        print('B Looking')

class C(A,B):   #C extends A,B
    def displayC(self):
        print('C Display')

c = C()
c.displayA()
c.displayB()
c.displayC()

#----- When Both the classes has same name method ------------

c.look()  #Output: A Looking (Precedence is given in the order of inheritance) 