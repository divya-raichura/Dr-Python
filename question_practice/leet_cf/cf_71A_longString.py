# my try
t = int(input())
while t != 0:
    s = input()
    if len(s) > 10:
        print(s[0] + str(len(s) - 2) + s[len(s) - 1])
    else:
        print(s)
    t = t - 1


# 71A - Way Too Long Words
# http://codeforces.com/problemset/problem/71/A

n = int(input())
for i in range(n):
    s = input()
    ans = s[0] + str(len(s) - 2) + s[-1] if len(s) > 10 else s
    print(ans)
