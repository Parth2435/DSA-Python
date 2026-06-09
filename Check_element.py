# Given an array, determine whether the value 9 exists in the array or not.

arr = [3, 7, 2, 9, 1]

i=0

arr_len = len(arr)

while i != arr_len:
    if arr[i] == 9:
        print("True")
        break

    i+=1

    if i == arr_len:
        print("False")

# 2nd more DSA like way:

# arr = [3, 7, 2, 9, 1]

# i=0

# arr_len = len(arr)

# found = False

# while i != arr_len:
#     if arr[i] == 9:
#         found = True
#         break

#     i += 1

# print(found)