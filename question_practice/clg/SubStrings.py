t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    count = 0
    for j in range(len(s)):
        if s[j] == "1":
            count += 1
    print(int((count*(count + 1)) / 2))

