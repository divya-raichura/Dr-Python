t = int(input())
while t > 0:
    d = dict()
    l = []
    n = int(input())
    for i in range(3):
        for j in range(n):
            temp = input()
            s, c = temp.split()
            c = int(c)
            d.setdefault(s, 0)
            d[s] += c

    for M in d.values():
        l.append(M)
    l_s = sorted(l)
    for Q in l_s:
        print(Q, end=' ')
    print()
    t -= 1

# how to take str and int input together and then separate them
# n = input()
# c, s = n.split()
# c = int(c)
