import random

arr = [random.randint(0, 10) for _ in range(10)]

min_value = min(arr)
max_value = max(arr)

first_min_index = arr.index(min_value)
last_max_index = len(arr) - 1 - arr[::-1].index(max_value)

print("Array:", arr)
print("First minimum index:", first_min_index)
print("Last maximum index:", last_max_index)