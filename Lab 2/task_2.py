def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


num_terms = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", fibonacci_sequence(num_terms))