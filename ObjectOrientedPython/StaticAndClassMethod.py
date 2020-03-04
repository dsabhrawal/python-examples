# class methods are always decorated with @classmethod
# Static methods can optionally be decorated with @staticmethod

class StaticExample:

    @staticmethod
    def sum(x,y):   #Static method as no ref passed of instance
        print(x+y)

    @classmethod   #If class method annotation is not applied it will be considered as instance method and first parameter will be considered as self ref
    def mul(cls,x,y): #class method as ref of cls is passed
        print(x*y)


StaticExample.sum(1,2)  #called static way prints 3
s = StaticExample()
s.sum(1,2)           #It gives error if decorator annotation is not applied as 
                    #it consider sum as instance method instead of static

s1 = StaticExample()
s1.mul(2,3)
