# We will learn to create parameterized constructor

class Employee:
    ''' This is the version 2.0 of Employee class'''
    def __init__(self,name,org,salary):
        super().__init__()
        self.name = name
        self.organisation = org
        self.salary = salary
    
    def __str__(self):
        return 'This is Employee class'
    
    def display(self):
        print('Employee Name: ',self.name)
        print('Employee Org: ',self.organisation)
        print('Employee Salary: ',self.salary)

#Creating diff instance of the Employee class
e1 = Employee('A','P',1000)
e2 = Employee('B','Q',2000)
e3 = Employee('C','R',3000)

e1.display()
e2.display()
e3.display()

#List of objects and call display in for loop
employees = [e1,e2,e3]
for e in employees:
    e.display()