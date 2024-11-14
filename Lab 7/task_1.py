arr = [1, 2, 3, 4, 5, 6]

if any(num % 3 == 0 for num in arr):
    print("There are numbers divisible by three in the array.")
else:
    print("There are no numbers divisible by three in the array.")