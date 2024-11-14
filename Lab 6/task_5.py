import random

array = [random.randint(-10, 10) for _ in range(20)]
min_value = int(input("Enter the minimum value of the range: "))
max_value = int(input("Enter the maximum value of the range: "))

indices = [i for i, value in enumerate(array) if min_value <= value <= max_value]

print("Array:", array)
print("Range:", f"[{min_value}; {max_value}]")
print("Count:", len(indices))
print("Indices:", indices)