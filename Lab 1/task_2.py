variable_1 = int(input("Enter the first variable: "))
variable_2 = int(input("Enter the second variable: "))

print(variable_1, "+", variable_2, "=", variable_1 + variable_2)
print(variable_1, "/", variable_2, "=", variable_1 / variable_2)
print(variable_1, "and", variable_2, "in binary:", bin(variable_1)[2:], "and", bin(variable_2)[2:])
print(variable_1, "and", variable_2, "in hexadecimal:", hex(variable_1)[2:], "and", hex(variable_2)[2:])
print(variable_1, "and", variable_2, "in octal:", oct(variable_1)[2:], "and", oct(variable_2)[2:])