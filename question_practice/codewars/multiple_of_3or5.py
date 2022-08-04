def solution1(number):
    if number <= 0:
        return 0
    three = int((number - 1) / 3)
    five = int((number - 1) / 5)
    ans = 0
    for i in range(1, three + 1):
        ans += 3 * i
    for i in range(1, five + 1):
        ans += 5 * i
    both = int(three / 5)
    both_sum = 0
    for i in range(1, both + 1):
        both_sum += 3 * 5 * i
    return ans - both_sum


def solution2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


print(solution1(16))
print(solution2(16))
