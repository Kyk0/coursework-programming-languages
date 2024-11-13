import random

arr = [random.randint(0, 4)for _ in range(10)]
x = int(input("Enter the value of X: "))

print("Array:", arr)
print("Indices:", [i for i in range(len(arr)) if arr[i] == x])