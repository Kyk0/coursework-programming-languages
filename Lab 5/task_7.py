expression = input("Enter the expression: ")
numbers = expression.split(' + ')
result = sum(int(num) for num in numbers)

print("Result:", result)