N = int(input("Enter the number of elements: "))
elements = []

for _ in range(N):
    elements.append(int(input("Enter a number: ")))

total_sum = sum(elements)
average = total_sum / N

print("Average:", average)