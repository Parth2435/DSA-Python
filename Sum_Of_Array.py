# Sum of the array:

arr = [3, 7, 2, 9, 1]

x = 0
i=0

len_arr = len(arr)

while i!= len_arr:
    x += arr[i]
    i+=1

print(x)

# Important Rule

# When analyzing space complexity:

# 1 variable     → O(1)
# 5 variables    → O(1)
# 100 variables  → O(1)

# As long as the number of variables does not grow with n, it's still O(1).

# What would become O(n)?

# Something like:

# new_arr = []

# for num in arr:
#     new_arr.append(num)

# Because the size of new_arr grows as the input grows.