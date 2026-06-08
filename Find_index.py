# Given array, find the index of number 9

arr = [3, 7, 2, 9, 1]

arr_len = len(arr)

i = 0

while i != arr_len:
    if arr[i] == 9:
        print(i)
    
    i += 1