# private variables are preceeded by __ ex __name

class Student:
    def setName(self,name):
        self.__name = name  #Setting value for private variable __name
    
    def getName(self):
        return self.__name

    def setRollno(self,rollno):
        self.__rollno = rollno  #setting value for private variable __rollno

    def getRollno(self):
        return self.__rollno

    def display(self):
        print('Name: ',self.getName())
        print('RollNo: ',self.getRollno())


s = Student()
#s.__name  # Error not visible
s.setName('ABC')
s.setRollno(101)

s.display()