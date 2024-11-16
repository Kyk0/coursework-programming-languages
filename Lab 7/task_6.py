import random

arr = [random.randint(0, 10) for _ in range(10)]
indices = list(range(len(arr)))

for i in range(len(indices)):
    for j in range(len(indices) - i - 1):
        if arr[indices[j]] > arr[indices[j + 1]]:
            indices[j], indices[j + 1] = indices[j + 1], indices[j]

print("Array:", arr)
print("Sorted indices:", indices)