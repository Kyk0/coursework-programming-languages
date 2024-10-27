def difference_global():
    global a, b
    print("Difference (global variables):", a - b)

def difference_parameters(x, y):
    print("Difference (parameters):", x - y)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

choice = input("1. Global variables\n2. Parameters\n Enter your choice: ")

if choice == "1":
    difference_global()
elif choice == "2":
    difference_parameters(a, b)
else:
    print("Invalid choice.")