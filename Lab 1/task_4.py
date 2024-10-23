import math

choice = int(input("Choose an option:\n"
                   "1.x=(0.51x^3+AB)/(1+cos^2(x))+A/(A+B)\n"
                   "2.x=(ae/c)+|(a-e)/cos(a)^3|\n"
                   "3.y=0.87*|a^2+sqrt(e)*a|/(x-1+(1+b)/(1-a))\n"
                   "4.y=sqrt(|x+sqrt(x^2)|/(1-2x))\n"
                   "5.y=((1+x)^2+sqrt(1+x^2))/cos^2(x)\n"
                   "6.y=0.5x-[(ax-e)+c](x-e)/(x-1)\n\n"
                   "Enter your choice: "))

if not 1 <= choice <= 6:
    exit("Invalid choice")

if choice == 1:
    A = float(input("Enter the value of A: "))
    B = float(input("Enter the value of B: "))
    x = float(input("Enter the value of x: "))
    result = (0.51 * x ** 3 + A * B) / (1 + math.cos(x) ** 2) + (A / (A + B))
    print(f"The result is {result}")

elif choice == 2:
    a = float(input("Enter the value of a: "))
    e = float(input("Enter the value of e: "))
    c = float(input("Enter the value of c: "))
    result = (a * e / c) + abs((a - e) / (math.cos(a) ** 3))
    print(f"The result is {result}")

elif choice == 3:
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    e = float(input("Enter the value of e: "))
    x = float(input("Enter the value of x: "))
    numerator = abs(a ** 2 + math.sqrt(e) * a)
    denominator = x - 1 + (1 + b) / (1 - a)
    result = 0.87 * (numerator / denominator)
    print(f"The result is {result}")

elif choice == 4:
    x = float(input("Enter the value of x: "))
    result = math.sqrt(abs(x + math.sqrt(x ** 2)) / (1 - 2 * x))
    print(f"The result is {result}")

elif choice == 5:
    x = float(input("Enter the value of x: "))
    numerator = (1 + x) ** 2 + math.sqrt(1 + x ** 2)
    denominator = math.cos(x) ** 2
    result = numerator / denominator
    print(f"The result is {result}")

elif choice == 6:
    a = float(input("Enter the value of a: "))
    e = float(input("Enter the value of e: "))
    c = float(input("Enter the value of c: "))
    x = float(input("Enter the value of x: "))
    numerator = ((a * x - e) + c) * (x - e)
    result = 0.5 * x - (numerator / (x - 1))
    print(f"The result is {result}")