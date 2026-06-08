# Write an algorith to check how many times a number has appeared in the array.

arr = [7, 1, 2, 3, 4, 7]

arr_len = len(arr)

i = 0
count = 0

while i != arr_len:
    if arr[i] == 7:
        count += 1

    i += 1

print("Times 7 appeared:", count)

# 2nd more python like way:

arr = [7, 1, 2, 3, 4, 7]

count = 0

for num in arr:
    if num == 7:
        count += 1

print("Times 7 appeared:", count)