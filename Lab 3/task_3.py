def print_divisors(number):
    divisors = [str(i) for i in range(1, number + 1) if number % i == 0]
    print("Divisors:", " ".join(divisors))

number = int(input("Enter a number: "))
print_divisors(number)