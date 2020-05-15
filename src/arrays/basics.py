import sys

def basics():
    arr = [1,2,3,4,5]
    print(arr)
    
    cars = ['Toyota','Tesla','Honda']    
    for x in cars:
        print(x)
    print(len(cars))

    arr = [4,7,9,3,2]
    arr.sort()
    print(arr)
    arr.reverse()
    print(arr)
    
    arr = ['a','b','a','b','a','b','a','b']
    print(arr)
    arr.remove('a')
    print(arr)
    arr.pop(0)
    print(arr)
    print(arr.count('b'))
    print(arr.index('b'))

basics()