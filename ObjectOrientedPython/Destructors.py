# Like constructor destructor is also called implicitly by python when object is not in use
# Destructor has __del__ in name

class Parent:
    def __init__(self):
        print('Constructor called')

    def show(self):
        print('show class method')

    def __del__(self):
        print('Destructor called')


P = Parent()
P.show()

#output
#Constructor called
#show class method
#Destructor called