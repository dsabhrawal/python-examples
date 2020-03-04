class Parent:
    def __init__(self):
        super().__init__()
        print('Parent Constructor')
    
    def displayParent(self):
        print('Parent Class Display')
    
    class Child:
        def __init__(self):
                super().__init__()
                print('Child Constructor')
        
        def displayChild(self):
            print('Child class display')


#Two ways to initialize and use inner class
#Direct Initialization using parent class

c = Parent().Child()
c.displayChild()

#Using instance of Parent
p = Parent()
p.displayParent()
#p.displayChild() # Error Not allowed
c1 = p.Child()
c1.displayChild()

