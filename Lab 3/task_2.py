def print_digits_reverse(number):
    print("result:")
    for digit in str(number)[::-1]:
        print(digit)

number = int(input("Enter a number: "))
print("number:", number)
print_digits_reverse(number)