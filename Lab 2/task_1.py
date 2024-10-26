positive_sum = 0
negative_sum = 0

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    elif number > 0:
        positive_sum += number
    else:
        negative_sum += number

print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")