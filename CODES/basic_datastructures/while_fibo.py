n = int(input("how many terms should the series have: "))
# 0 1 1 2 3 5 8 13 21 ...
a = 0
b = 1
count = 0
termNo = 0
while count <= n:
    print(a, end=' ')
    count += 1
    temp = b
    b = a + b
    a = temp
    termNo += 1
    # no need to create temp... simply do
    # a, b = b, a + b
print()
print(termNo)


