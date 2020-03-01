# We have to use the built in sys module to use command line arguments
import sys

#argv is the variable we have to use
#argv[0] - FileName
#argv[1] - First Parameter 
#argv[2] - Second Parameter and so on 

print(len(sys.argv)) #Prints 1 if no arguments is passed
print(sys.argv[0]) #Prints name of the file
print(sys.argv[1]) #First argument
print(sys.argv[2]) #Second argument