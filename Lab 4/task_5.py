first_element = int(input("Enter first element: "))
difference = int(input("Enter difference: "))
count = int(input("Enter count: "))

progression = [first_element + i * difference for i in range(int(count))]
print(progression)