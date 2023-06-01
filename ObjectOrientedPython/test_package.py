#Here we will import calculator module from the custom package

#If you see no myfirstpackage module found error make sure your project directory is
#on the class path
#hit this on command prompt with proper path of your project directory
#export PYTHONPATH="${PYTHONPATH}:/path/to/your/project"

from myfirstpackage import calculator as calc

print(calc.sum(2,3))

print(calc.mul(2,3))

