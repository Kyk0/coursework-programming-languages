import random

rows, cols = 3, 4
matrix = [[random.randint(-30, 30) for _ in range(cols)] for _ in range(rows)]

min_value = matrix[0][0]
max_value = matrix[0][0]
min_index = (0, 0)
max_index = (0, 0)

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_index = (i, j)
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_index = (i, j)

print("Matrix:")
for row in matrix:
    print(row)
print("Minimum value:", min_value, "at index:", min_index)
print("Maximum value:", max_value, "at index:", max_index)