# Program to print factorial of a number using recurssion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

x = int(input('Enter a number: '))
print('Factorial of {} is {}'.format(x,factorial(x)))
