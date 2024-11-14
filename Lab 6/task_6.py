import random

array = [random.randint(-10, 10) for _ in range(20)]
min_value = int(input("Enter the minimum value of the range: "))
max_value = int(input("Enter the maximum value of the range: "))

indices = []
i = 0

while i < len(array):
    if min_value <= array[i] <= max_value:
        indices.append(i)
        array.pop(i)
    else:
        i += 1

print("Modified Array:", array)
print("Count of indices:", len(indices))
print("Indices:", indices)