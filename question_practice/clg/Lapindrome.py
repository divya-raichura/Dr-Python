t = int(input())
for x in range(t):
    d = dict()
    s = input()
    m = len(s) // 2
    if len(s) % 2 != 0:
        s = s[:m] + s[m + 1:]
        m = len(s) // 2
    for i in range(len(s)):
        d.setdefault(s[i], 0)
        d[s[i]] += 1

    flag = 0
    for i in d.values():
        if i % 2 != 0:
            flag = -1
            break

    if flag == 0:
        print("YES")
    else:
        print("NO")


