# my try
s = input()
print(chr(ord(s[0]) - 32) + s[1:] if ord(s[0]) >= 97 else s)

# print(s.capitalize())
# 65 A, 97 a

# 281A - Word Capitalization
# http://codeforces.com/problemset/problem/281/A

s = input()
print(s[0].upper() + s[1:])
