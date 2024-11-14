lst = [4, 5, 2, 3, 4]
minimum = min(lst)
maximum = max(lst)
total = sum(lst)
average = total / len(lst)
second_minimum = min(x for x in lst if x != minimum)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", average)
print("Second minimum:", second_minimum)