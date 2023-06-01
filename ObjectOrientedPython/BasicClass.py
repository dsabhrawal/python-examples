#Class can be defined with keyword class
#Variables and methods are indented same as in functions
#Basic structure of class is as follow:
#class ClassName:
#   "This is version 1.0"  -- Optional documentation string
#   (Variables)
#   Instance Variables, Static Variables, Local Variables
#   (Methods)
#   Instance Methods, Static Methods, Class Methods

#Functions are written outside the class
#Methods are written inside the class

class Employee:
    ''' This is the version 1.0 of Employee class''' #doc string
    #Defining constructor of class Employee 
    #self refers to the current object (same like this in java programming)
    #any variable defined with self is an instance variable in python
    def __init__(self):
        super().__init__()
        self.name = 'EmployeeA' #Instance Variable name
        self.organisation = 'OrgA' #Instance Variable organisation
        self.salary = '100000'  #Instance Variable salary
    
    def __str__(self):
        return 'This is Employee class'
    
    def display(self):
        print('Employee Name: ',self.name)
        print('Employee Org: ',self.organisation)
        print('Employee Salary: ',self.salary)


#Following code is not indented hence, not part of the class code
e = Employee() #Constructor is called and variables will be initialized
print(e.name)   #Output: EmployeeA
print(e.organisation) #Output: OrgA
print(e.salary) #Output: 100000
print(e.__doc__)  #Output: This is the version 1.0 of Employee class
print(e)  #Output: This is Employee class

#Explicitly call the constructor method
e.__init__()

# call display method to print class variable values
e.display()
#Output:
#Employee Name:  EmployeeA
#Employee Org:  OrgA
#Employee Salary:  100000

#Important Notes:
#self is not a keyword or reserved word in python
#we can use any name instead of self like this
#The first parameter paased to any instance method is pointing to the current object
