# Instance variables should be initialized before use
# There are three ways to initialize instance variables
# 1. Using Constructor 2. Using object 3. Using methods

class Student:
    #Initializing using constructor
    def __init__(self,name):
        super().__init__()
        self.name = name

    #Initializing using methods
    def defineAttributes(self,roll_no, age):
        self.roll_no = roll_no
        self.age = age
    
    def display(self):
        print('Name: ',self.name)
        print('RollNo: ',self.roll_no)
        print('Age: ',self.age)
        print('Section: ',self.section)

s = Student('Student_A') #only name is initialized

#s.display() #will result into error 
s.section='B' #section is initialized
s.defineAttributes(113,15) #roll no and age is initialized

s.display()

#Symbol table or special attribute __dict__ (holds dictionary of the instance variables)
print(s.__dict__)  #Output: {'name': 'Student_A', 'section': 'B', 'roll_no': 113, 'age': 15}

#Deleting instance variables
del s.age
print(s.__dict__) #Output: {'name': 'Student_A', 'section': 'B', 'roll_no': 113}
