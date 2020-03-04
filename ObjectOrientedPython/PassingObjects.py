
class Student:
    def __init__(self, name, marks, clg):
        super().__init__()
        self.name = name
        self.marks = marks
        self.clg = clg
    
    def display(self):
        print('Name: ',self.name)
        print('Marks: ',self.marks)
        self.clg.display()

class College:
    def __init__(self, name, reg_no):
        super().__init__()
        self.name = name
        self.reg_no = reg_no

    def display(self):
        print('Clg Name: ',self.name)
        print('Clg Registration: ', self.reg_no)

c = College('College A', 101)
s = Student('Student A', 78, c)
s.display()

#Output
#Name:  Student A
#Marks:  78
#Clg Name:  College A
#Clg Registration:  101