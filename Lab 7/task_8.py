import random

arr = [random.randint(0, 10) for _ in range(15)]

series_lengths = []
series_values = []

current_length = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        current_length += 1
    else:
        series_lengths.append(current_length)
        series_values.append(arr[i - 1])
        current_length = 1
series_lengths.append(current_length)
series_values.append(arr[-1])

print("Original array:", arr)
print("Series lengths:", series_lengths)
print("Series values:", series_values)