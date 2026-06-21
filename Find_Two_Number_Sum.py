# Find Two Numbers That Sum to a Target: Given: arr = [2, 7, 11, 15], target = 9. Expected output: 2 + 7 = 9 or the indices: 0, 1

arr = [21, 7, 2, 15]

target = 9

val1 = 0

val2 = 0

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        sum_of_two =  arr[i] + arr[j]
        if sum_of_two == target:
            x = i
            y = j
            val1 = arr[i]
            val2 = arr[j]

print("Indices: ", x, y)
print("Values: ", val1, val2)