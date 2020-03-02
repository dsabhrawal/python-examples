# Local Variables are defined and used inside functions
# Local variables have life cycle within the function execution
# Global variables are accessed and modified accross functions

#Local Variable
def ex_local_var():
    a = 10 #Local
    print(a)

def ex_local_var1():
    a = 20 #Local
    print(a)

ex_local_var() #10
ex_local_var1() #20

print('\n\n\n')
# Global Variable

x = 20
print(x) # 20

def ex_local_var2():
    global x #Global
    x = 50

def ex_local_var3():
    global x #Global 
    x = 30

ex_local_var2()
print(x) # 50 (changed by funciton ex_local_var2())
ex_local_var3()
print(x) # 30

