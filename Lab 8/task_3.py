import random

rows, cols = 3, 4
matrix = [[random.randint(-30, 30) for _ in range(cols)] for _ in range(rows)]

max_sum = sum(matrix[0])
max_sum_row = matrix[0]

for row in matrix[1:]:
    row_sum = sum(row)
    if row_sum > max_sum:
        max_sum = row_sum
        max_sum_row = row

print("Matrix:")
for row in matrix:
    print(row)
print("Row with maximum sum:", max_sum_row)