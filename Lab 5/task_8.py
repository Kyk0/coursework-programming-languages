S = input("Enter the string: ")
L = len(S)
flag = 1

for i in range(L // 2):
    if S[i] == S[L - i - 1]:
        k = 1
    else:
        k = 0
    flag *= k

if flag == 1:
    res = "Palindrome"
else:
    res = "Not a palindrome"

print(res)