def print_fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = []
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    print("Fibonacci sequence:", " ".join(map(str, fibonacci_sequence)))

n = int(input("Enter a natural number N: "))
print_fibonacci(n)