# Static variables are class level variables
# Static variables are always referenced by class name
# Local variables are local to methods

class Student:
    school = 'PQR'  #Static variable
    def __init__(self,name,roll,section):
        super().__init__()
        self.name = name  #Instance variable
        self.roll = roll
        self.section = section
    
    def display(self):
        school = 'Local School'
        print('Name of student: ',self.name)
        print('Roll No of student: ',self.roll)
        print('Section of Student: ',self.section)
        print('School of Student: ', Student.school) #Static variable
        print('Local school value: ', school)

#Student.school = 'ABC School' #Another way to declare static variables
s1 = Student('Student A',101,'A')
s2 = Student('Student B',102,'B')
s1.display()
s2.display()
