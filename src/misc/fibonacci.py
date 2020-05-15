import sys

def fibonacci(val):
    if val <= 1: 
        return val
    
    return fibonacci(val - 1) + fibonacci(val - 2)
    
num = int(input('Enter num : '))
if num < 0:
    print('Error : Invalid input')
else:
    for i in range(num):
        fib = fibonacci(i)
        sys.stderr.write(str(fib) + ',')

sys.stderr.write('\n')
