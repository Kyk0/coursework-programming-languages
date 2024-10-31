text = "Extract the following slices from the string: the first eight characters, four characters from the center of the string, five characters from the end of the string."

first_eight = text[:8]
center_four = text[len(text) // 2 - 2 : len(text) // 2 + 2]
last_five = text[-5:]

print("First eight characters:", first_eight)
print("Four characters from the center:", center_four)
print("Five characters from the end:", last_five)