# https://atcoder.jp/contests/abc189/tasks/abc189_b

n, x = map(int, input().split())
limit, i = 0, 0
while n != i:
    v, p = map(int, input().split())
    limit += v * p
    i += 1
    if limit > x*100:
        print(i)
        break
else:
    print(-1)
