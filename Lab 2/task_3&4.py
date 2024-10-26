import random

choice = input("1. Random input\n2. Manual input\nEnter your choice: ")
numbers = []

if choice == "1":
    size = random.randint(1, 100)
    numbers = list(range(1, size + 1))
    for i in range(size):
        numbers[i] = random.randint(1, 1000)

if choice == "2":
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

average = sum(numbers) / len(numbers) if numbers else 0
print("Average:", average)