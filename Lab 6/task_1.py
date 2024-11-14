s = input("Enter the string: ")
l = list(s)
result = sum(int(num) for num in ''.join(l).split('+'))
print("Result:", result)