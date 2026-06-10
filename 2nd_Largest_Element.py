# Find the 2nd largest element of the array.

# arr = [3, 7, 2, 9, 1]

# largest = 0

# i = 0

# while i != len(arr):
#     if arr[i] > largest:
#         largest = arr[i]
    
#     i+=1
    
# second_largest = 0

# j=0

# while j != len(arr):
#     if arr[j] > second_largest and arr[j] != largest:
#         second_largest = arr[j]

#     j+=1

# print(second_largest)

# 2nd way which doesn't use 2 loops (More DSA like approach):

arr = [3, 7, 2, 9, 1]

i = 0

largest = arr[0]

second_largest = arr[0]

while i != len(arr):
    if arr[i] > second_largest and arr[i] > largest:
        second_largest = largest
        largest = arr[i]

    elif arr[i] > second_largest and arr[i] < largest:
        second_largest = arr[i]
    
    i += 1

print(second_largest)