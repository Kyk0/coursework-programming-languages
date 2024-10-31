text = "Given a string of length N, output the even-indexed characters first, then the odd-indexed characters."

even_index_chars = text[1::2]
odd_index_chars = text[0::2]

print("Characters with even indices:", even_index_chars)
print("Characters with odd indices:", odd_index_chars)