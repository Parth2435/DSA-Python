# Reverse the given array.

arr = [3, 7, 2, 9, 1]

left = 0
right = len(arr) - 1

while left < right:
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    left+=1
    right-=1

print(arr)