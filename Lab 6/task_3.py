import random
from sympy import isprime

array = [random.randint(1, 10) for _ in range(10)]
primes = [num for num in array if isprime(num)]

print("Array:", array)
print("Primes:", primes)