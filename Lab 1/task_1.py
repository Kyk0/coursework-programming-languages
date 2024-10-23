
def task_1():
    choice = int(input("Choose an option: "
                       "1. 20a^3*(5a)^2\n"
                       "2. -0,4x^5*(2x^3)^4\n"
                       "3. (-3c^3)^2*12c^6\n"
                       "4. (3x^6y^3)^4*(-(1/81)*xy^2)\n"
                       "5. (-(2/3)ab^5)^3*18a^5b\n\n"
                       "Enter your choice: "))

    if not 1 <= choice <= 5:
        exit("invalid choice")

    if choice == 1:
        a = float(input("Enter the value of a: "))
        result = 20 * a ** 3 * (5 * a) ** 2
        print(f"The result is {result}")

    elif choice == 2:
        x = float(input("Enter the value of x: "))
        result = -0.4 * x ** 5 * (2 * x ** 3) ** 4
        print(f"The result is {result}")

    elif choice == 3:
        c = float(input("Enter the value of c: "))
        result = (-3 * c ** 3) ** 2 * 12 * c ** 6
        print(f"The result is {result}")

    elif choice == 4:
        x = float(input("Enter the value of x: "))
        y = float(input("Enter the value of y: "))
        result = (3 * x ** 6 * y ** 3) ** 4 * (-(1 / 81) * x * y ** 2)
        print(f"The result is {result}")

    elif choice == 5:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        result = (-(2 / 3) * a * b ** 5) ** 3 * 18 * a ** 5 * b
        print(f"The result is {result}")



task_1()