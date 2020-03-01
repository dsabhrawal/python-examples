# We will discuss if / else / elif (else if)

x = 10
y = 20

if x<y:
    print('X is less than y')
    print('Hurrey! If statement executed.')
else:
    print('x is greater than y')
    print('Hurrey! else statement executed')

print('Hurrey! program completed!')

#elif
#User will enter two numbers and we have to identify if both are
#equal or which number is less than other

p = eval(input('Enter first Number:'))
q = eval(input('Enter second number:'))

if p>q:
    print('First Number {} is greater than second number {}'.format(p,q))
elif p<q:
    print('First Number {} is less than second number {}'.format(p,q))
else:
    print('First Number {0} is Equals to second Number{1}'.format(p,q))