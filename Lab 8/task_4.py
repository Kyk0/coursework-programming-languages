import random

N = 5
matrix = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

min_below_diagonal = None
for i in range(1, N):
    for j in range(N - i, N):
        if min_below_diagonal is None or matrix[i][j] < min_below_diagonal:
            min_below_diagonal = matrix[i][j]

last_row_nonzero_product = 1
for value in matrix[-1]:
    if value != 0:
        last_row_nonzero_product *= value

print("Matrix:")
for row in matrix:
    print(row)
print("Minimum element below the secondary diagonal:", min_below_diagonal)
print("Product of non-zero elements in the last row:", last_row_nonzero_product)