# Left Rotate an array by the given number
# arr = [5,3,6,9,2,8]
# left_rotate(arr,2)
# Result : [6,9,2,8,5,3]

def left_rotate(arr,d):
    for i in range(0,d):
        x = arr.pop(0)
        arr.append(x)

arr = [5,3,6,9,2,8]
print(arr)
left_rotate(arr,2)
print(arr)

# Right Rotate an array by the given number
# arr = [5,3,6,9,2,8]
# right_rotate(arr,2)
# [2,8,5,3,6,9]
def right_rotate(arr,d):
    n = len(arr)
    for i in range(0,d):
        x = arr.pop(n-1)
        arr.insert(0,x)

arr = [5,3,6,9,2,8]
print(arr)
right_rotate(arr,2)
print(arr)
