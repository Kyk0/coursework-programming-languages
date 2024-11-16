import random

arr = [random.randint(0, 10) for _ in range(10)]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

unique_count = 1
for i in range(1, n):
    if arr[i] != arr[i - 1]:
        unique_count += 1

print("Sorted array:", arr)
print("Number of unique numbers:", unique_count)