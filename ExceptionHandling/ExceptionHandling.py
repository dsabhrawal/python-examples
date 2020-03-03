#Common exceptions are
#ImportError | IndexError | NameError | TypeError | ValueError | IOError
# Standard errors are defined in exceptions module

items = [10,20,30,40,50]

print(items[2]) #30
print(items)  #Content of List

#------------------------
#Exception handling of IndexError

try:
    print(items[10]) #IndexError Handled
except IndexError as e:
    print(e) #list index out of range

print(items) #list items printed

#We can use except Exception if we are not sure about the particular exception type

try:
    print(items[15]) #IndexError Handled
except Exception as e:
    print(e) #list index out of range

print(items) #list items printed