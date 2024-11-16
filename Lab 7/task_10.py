import random

arr = [random.randint(0, 10) for _ in range(10)]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

max_repeated = None
for i in range(1, n):
    if arr[i] == arr[i - 1]:
        if max_repeated is None or arr[i] > max_repeated:
            max_repeated = arr[i]

print("Sorted array:", arr)
print("Maximum repeated number:", max_repeated)